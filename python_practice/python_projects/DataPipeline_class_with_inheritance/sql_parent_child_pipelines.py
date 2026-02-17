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
        self.log_status("Reading CSV from S3 bucket...")
        # Simulating CSV rows
        self.raw_data = [
            {"Campaign_ID": "FB_001", "Spend": 150.00},
            {"Campaign_ID": "FB_002", "Spend": 200.50}
        ]

class GooglePipeline(MarketingPipeline):
    def extract(self):
        self.log_status("Calling Google Ads API...")
        # Simulating JSON response
        self.raw_data = [
            {"id": "G_99", "cost": 300.25},
            {"id": "G_88", "cost": 10.00}
        ]

    def transform(self):
        # 1. Use inheritance to do the basic cleaning first
        super().transform() 
        
        # 2. Add Google-specific logic: Rename 'id' to 'campaign_id'
        self.log_status("Renaming Google-specific fields...")
        for record in self.cleaned_data:
            if 'id' in record:
                record['campaign_id'] = record.pop('id')

class TwitterPipeline(MarketingPipeline):
    def extract(self):
        self.log_status("enterning twitter data ...")
        self.raw_data = [
            {"twitter_id": "T_33", "cost": 300.25},
            {"twitter_id": "T_88", "cost": 10.00}
        ]
    def transform(self):
        super().transform() 
        self.log_status("Renaming twitter-specific fields...")
        for record in self.cleaned_data:
            if 'twitter_id' in record:
                record['campaign_id'] = record.pop('twitter_id')


if __name__ == "__main__":
    print("--- TESTING PIPELINES ---")
    
    # 1. Test the Facebook Pipeline
    fb_job = FacebookPipeline("Facebook_Ads")
    fb_job.run()
    
    print("\n" + "="*30 + "\n")
    
    # 2. Test the Google Pipeline
    google_job = GooglePipeline("Google_Ads")
    google_job.run()

    twitter_job = TwitterPipeline("Twitter_comments")
    twitter_job.run()


## to see the data from sqllite3 -- sqlite3 marketing_data.db "SELECT * FROM ads_data;"
## postgresql psql -h localhost -U your_username -d marketing_db -c "SELECT * FROM ads_data;"