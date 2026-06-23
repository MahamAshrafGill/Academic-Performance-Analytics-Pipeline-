import pandas as pd

def audit_and_clean_data(df)
    print("[AUDIT] Starting securing data integrity checks.....")
    
    corrupted_data = df[
        (df['study_hours_per_day']>24) |
        (df['exam_score']<0)|
        (df['attendance_percentage']>100)
    ]

    clean_data = df[
        (df['study_hours_per_day']<=24) &
        (df['exam_score']>=0) &
        (df['attendance_percentage']<=100)
    ]

    if not corrupted_data.empty:
        print(f"[ALERT] Security anomaly detected! Found {len(corrupted_data)} corrupted records.")
        corrupted_data.to_csv("corrupted_audit_log.csv", index = False)
        print("[LOG] Corrupted files successfully logged to 'corrupted_audit_log.csv'" )
    else:
        print("[SUCCESS] All clear! No data integrity issue found.")
    
    return clean_data