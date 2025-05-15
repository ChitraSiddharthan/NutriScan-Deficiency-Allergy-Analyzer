from .data import SYMPTOM_CONDITION_MAPPING, MEDICAL_HISTORY_IMPACT, DEFAULT_RESPONSE
#defining the analyze_symptoms to package as a library
def analyze_symptoms(symptoms, medical_history):
    overall_severity = "Mild"
    predicted_conditions = set() 
    recommendations = set()

    # 1. below code checks MEDICAL HISTORY IMPACT first 
    for condition_name, history_data in MEDICAL_HISTORY_IMPACT.items():
        if condition_name.lower() in medical_history: # Case-insensitive match for medical history
            for symptom_in_history, condition_details in history_data.items():
                if symptom_in_history.lower() in symptoms: # Case-insensitive match for symptoms
                    predicted_conditions.add(condition_details["condition"]) # Adds condition to set
                    recommendations.add(condition_details["recommendation"]) # Adds recommendation
                    condition_severity = condition_details["severity"]
                    severity_levels_order = {"Mild": 1, "Moderate": 2, "Severe": 3, "Unknown": 0}
                    highest_severity_level = severity_levels_order.get(overall_severity, 1) # This line, Defaults to 'Mild' if current severity is invalid
                    if severity_levels_order[condition_severity] > highest_severity_level:
                        overall_severity = condition_severity


    # 2. Then, we will check SYMPTOM-BASED conditions for any remaining symptoms
    for symptom in symptoms:
        symptom_lower = symptom.lower() # Case-insensitive matching for symptoms, it converts input to lowercases
        if symptom_lower in SYMPTOM_CONDITION_MAPPING:
            condition_data = SYMPTOM_CONDITION_MAPPING[symptom_lower]
            predicted_conditions.add(condition_data["condition"]) # Add condition to set
            recommendations.add(condition_data["recommendation"]) # Add recommendation
            condition_severity = condition_data["severity"]
            severity_levels_order = {"Mild": 1, "Moderate": 2, "Severe": 3, "Unknown": 0}
            highest_severity_level = severity_levels_order.get(overall_severity, 1) # Default to 'Mild' if current severity is invalid
            if severity_levels_order[condition_severity] > highest_severity_level:
                overall_severity = condition_severity


    # 3. Handles case where no conditions were found at all
    if not predicted_conditions: # Check if the set is empty
        predicted_conditions = [DEFAULT_RESPONSE["condition"]] # Use default condition
        recommendations = [DEFAULT_RESPONSE["recommendation"]] # Use default recommendation
        overall_severity = DEFAULT_RESPONSE["severity"] # Use default severity

    #finally, below code converts it to JSON for conditions, severity, recommendation
    return {
        "conditions": list(predicted_conditions), # Converts set to list for JSON
        "severity": overall_severity,
        "recommendation": list(recommendations), # Converts set to list for JSON
    }

