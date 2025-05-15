# user_management/symptom_analysis/data.py

# symptom_to_condition = {
#     "sneezing": ["Dust Allergy", "Pollen Allergy"],
#     "itchy skin": ["Eczema", "Food Allergy"],
#     "headache": ["Vitamin D Deficiency", "Sinus Allergy"],
#     "fatigue": ["Iron Deficiency", "Vitamin B12 Deficiency"],
#     "hives": ["Insect Allergy", "Food Allergy"],
#     "nausea": ["Lactose Intolerance", "Food Sensitivity"],
#     "shortness of breath": ["Asthma", "Pollen Allergy"],
#     "skin rash" : ["skin allergy", "Dust Allergy"],
#     "itching": ["Pollen Allergy", "Dust Allergy"],
#     "chest pain": ["Heart Disease", "Gastritis"],
# }

# data.py
"""Data for analyzing symptom"""
# Mapping of symptoms to conditions, severity, and recommendations
SYMPTOM_CONDITION_MAPPING = {
    "fever": {
        "condition": "Flu",
        "severity": "Moderate",
        "recommendation": "Stay hydrated, rest, and monitor temperature."
    },
    "headache": {
        "condition": "Migraine",
        "severity": "Severe",
        "recommendation": "Avoid bright lights, stay hydrated, and rest."
    },
    "fatigue": {
        "condition": "Anemia",
        "severity": "Moderate",
        "recommendation": "Increase iron intake through diet or supplements."
    },
    "chest pain": {
        "condition": "Heart Disease",
        "severity": "Severe",
        "recommendation": "Seek immediate medical attention."
    },
    "cough": {
        "condition": "Bronchitis",
        "severity": "Moderate",
        "recommendation": "Rest, drink warm liquids, and consider cough suppressants."
    },
    "sore throat": {
        "condition": "Strep Throat",
        "severity": "Moderate",
        "recommendation": "Gargle with warm salt water, rest, and consult a doctor for antibiotics if needed."
    },
    "runny nose": {
        "condition": "Common Cold",
        "severity": "Mild",
        "recommendation": "Rest, drink fluids, and use a humidifier."
    },
    "muscle aches": {
        "condition": "Body Ache", # More general term
        "severity": "Mild",
        "recommendation": "Rest and consider over-the-counter pain relievers."
    },
    "nausea": {
        "condition": "Gastritis",
        "severity": "Moderate",
        "recommendation": "Eat bland foods, stay hydrated, and avoid spicy or greasy meals."
    },
    "dizziness": {
        "condition": "Vertigo",
        "severity": "Moderate",
        "recommendation": "Rest in a dark, quiet room and avoid sudden movements."
    },
    "skin rash": {
        "condition": "Eczema",
        "severity": "Mild",
        "recommendation": "Use moisturizer and avoid scratching. Consult a doctor if it worsens."
    },
    "itching": {
        "condition": "Allergic Reaction",
        "severity": "Mild", # Could be moderate to severe depending on cause
        "recommendation": "Avoid potential allergens and consider antihistamines."
    },
    "shortness of breath": {
        "condition": "Asthma Exacerbation",
        "severity": "Severe",
        "recommendation": "Use inhaler immediately and seek medical attention if symptoms don't improve."
    },
    "swelling": {
        "condition": "Edema",
        "severity": "Moderate", # Can vary greatly in severity depending on cause
        "recommendation": "Elevate the affected area and consult a doctor to determine the cause."
    },
    "palpitations": {
        "condition": "Arrhythmia",
        "severity": "Moderate", # Can be severe depending on type of arrhythmia
        "recommendation": "Avoid stimulants like caffeine and alcohol, and consult a cardiologist."
    },
    "blurred vision": {
        "condition": "Eye Strain",
        "severity": "Mild",
        "recommendation": "Rest your eyes, ensure proper lighting, and get your eyes checked if persistent."
    },
    "joint pain": {
        "condition": "Arthritis",
        "severity": "Moderate", # Can be severe depending on type and flare-up
        "recommendation": "Apply heat or cold packs, rest, and consider pain relievers. Consult a rheumatologist for chronic issues."
    },
    "insomnia": {
        "condition": "Stress-related Insomnia",
        "severity": "Mild", # Can become moderate to severe if chronic
        "recommendation": "Practice relaxation techniques, maintain a regular sleep schedule, and limit screen time before bed."
    }
}

# Medical history impact on symptoms
MEDICAL_HISTORY_IMPACT = {
    "diabetes": {
        "fatigue": {
            "condition": "Diabetic Fatigue",
            "severity": "Severe",
            "recommendation": "Monitor blood sugar levels and consult a doctor."
        },
        "wound healing issues": {
            "condition": "Delayed Wound Healing",
            "severity": "Moderate",
            "recommendation": "Keep wounds clean and monitor blood sugar levels."
        },
        "frequent urination": {
            "condition": "Uncontrolled Diabetes",
            "severity": "Moderate",
            "recommendation": "Check blood sugar and consult doctor about medication adjustments."
        }
    },
    "hypertension": {
        "chest pain": {
            "condition": "Hypertensive Heart Condition", # More descriptive condition
            "severity": "Severe",
            "recommendation": "Seek immediate medical attention."
        },
        "headache": {
            "condition": "Hypertensive Headache",
            "severity": "Moderate",
            "recommendation": "Monitor blood pressure and avoid stress."
        },
        "dizziness": {
            "condition": "Hypertensive Dizziness",
            "severity": "Moderate",
            "recommendation": "Sit or lie down slowly, monitor blood pressure."
        }
    },
    "asthma": {
        "shortness of breath": {
            "condition": "Asthma Exacerbation",
            "severity": "Severe",
            "recommendation": "Use inhaler immediately and seek medical help."
        },
        "cough": {
            "condition": "Asthmatic Cough",
            "severity": "Moderate",
            "recommendation": "Use inhaler as prescribed and avoid triggers."
        },
        "wheezing": {
            "condition": "Asthma Attack", # More serious condition
            "severity": "Severe",
            "recommendation": "Use rescue inhaler and seek emergency medical attention if severe."
        }
    },
    "allergies": { # General allergy history
        "itching": {
            "condition": "Allergic Itching",
            "severity": "Mild",
            "recommendation": "Avoid allergen and consider antihistamines."
        },
        "sneezing": {
            "condition": "Allergic Rhinitis",
            "severity": "Mild",
            "recommendation": "Avoid allergens, use nasal saline and antihistamines."
        },
        "skin rash": {
            "condition": "Allergic Dermatitis",
            "severity": "Mild", # Can be moderate if severe rash
            "recommendation": "Avoid allergen, use topical creams, consult dermatologist if severe."
        }
    }
}

# Default response if symptom is unknown
DEFAULT_RESPONSE = {
    "condition": "Unknown Condition",
    "severity": "Mild",
    "recommendation": "Consult a doctor for further diagnosis."
}
