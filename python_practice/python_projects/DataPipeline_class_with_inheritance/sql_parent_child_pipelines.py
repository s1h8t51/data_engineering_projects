import datetime
import sqlite3

class MarketingPipeline:
    def __init__(self, platform_name, db_name="marketing_data.db"):
        self.platform = platform_name
        self.db_name = db_name
        self.raw_data = []
        self.cleaned_data = []
        self._create_table() # Ensure the table exists when we start

    def _create_table(self):
        """Creates the SQL table if it doesn't exist yet."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # We create a generic table to hold our marketing records
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ads_data (
                platform TEXT,
                campaign_id TEXT,
                cost REAL,
                ingested_at TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_status(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.platform}] {message}")

    def transform(self):
        self.log_status("Starting transformation...")
        for record in self.raw_data:
            clean_record = {k.lower(): v for k, v in record.items()}
            clean_record['ingested_at'] = datetime.datetime.now().isoformat()
            self.cleaned_data.append(clean_record)

    def validate(self):
        self.log_status("Starting validation...")
        for row in self.cleaned_data:
            # Check for spend OR cost keys
            value = row.get('spend') or row.get('cost') or 0
            if value < 0:
                self.log_status(f"ALERT: Negative value detected: {value}")
                return False
        return True

    def load(self):
        """Saves the cleaned data into the SQLite database."""
        self.log_status(f"Loading {len(self.cleaned_data)} rows to SQL...")
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        for row in self.cleaned_data:
            # We map our dictionary keys to our SQL columns
            # Using ? prevents "SQL Injection" (a major security rule!)
            cursor.execute('''
                INSERT INTO ads_data (platform, campaign_id, cost, ingested_at)
                VALUES (?, ?, ?, ?)
            ''', (
                self.platform, 
                row.get('campaign_id') or row.get('campaign_id'), # Simplified for example
                row.get('spend') or row.get('cost'), 
                row.get('ingested_at')
            ))
        
        conn.commit()
        conn.close()
        self.log_status("Database Load Complete.")

    def run(self):
        # Reset state for fresh run
        self.raw_data = []
        self.cleaned_data = []
        
        self.extract()
        self.transform()
        if self.validate():
            self.load()
        else:
            self.log_status("Run aborted: Validation failed.")

# --- Child classes (Facebook, Google, etc) remain the same ---
class FacebookPipeline(MarketingPipeline):
    def extract(self):
        self.log_status("Reading CSV...")
        self.raw_data = [{"Campaign_ID": "FB_101", "Spend": 450.00}]

if __name__ == "__main__":
    fb_job = FacebookPipeline("Facebook")
    fb_job.run()
