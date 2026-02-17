import datetime

class MarketingPipeline:
    def __init__(self, platform_name):
        self.platform = platform_name
        self.raw_data = []
        self.cleaned_data = []

    def log_status(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.platform}] {message}")

    def extract(self):
        raise NotImplementedError("Each platform must have its own extraction logic!")

    def transform(self):
        """Common logic: lowercase all fields and add 'ingested_at' timestamp."""
        self.log_status("Starting transformation...")
        for record in self.raw_data:
            clean_record = {k.lower(): v for k, v in record.items()}
            clean_record['ingested_at'] = datetime.datetime.now().isoformat()
            self.cleaned_data.append(clean_record)

    def load(self):
        self.log_status(f"Loading {len(self.cleaned_data)} rows to PostgreSQL.")
        # Simulating Database Insert
        for row in self.cleaned_data:
            print(f"   -> DB INSERT: {row}")
    
    def validate(self):
        self.extract("starting validation...")
        for row in self.cleaned_data:
            value = row.get('spend') or row.get('cost') or 0
            if value < 0:
                self.log_status(f"ALERT: Negative value detected: {value}")
                return False
        return True

    def run(self):
        self.extract()
        self.transform()
        self.load()
        self.validate()
        if self.validate():
            self.load()
        else:
            self.log_status("Run aborted due to validation failure.")

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
                record['campaign_id'] = record.pop('twitter_id')

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


# ... your classes are above this ...

if __name__ == "__main__":
    print("--- TESTING PIPELINES ---")
    
    # 1. Test the Facebook Pipeline
    fb_job = FacebookPipeline("Facebook_Ads")
    fb_job.run()
    
    print("\n" + "="*30 + "\n")
    
    # 2. Test the Google Pipeline
    google_job = GooglePipeline("Google_Ads")
    google_job.run()
