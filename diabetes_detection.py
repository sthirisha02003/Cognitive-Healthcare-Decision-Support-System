from ocr_model import extract_text, extract_values

def predict_diabetes(image_path):
    text = extract_text(image_path)
    hba1c, glucose = extract_values(text)

    if hba1c is None or glucose is None:
        return "Could not detect values properly"

    if hba1c < 5.7:
        return "Normal"
    elif hba1c < 6.5:
        return "Prediabetes"
    else:
        return "Diabetes Detected"


if __name__ == "__main__":
    image_path = "sample_report.png"  # put your image here
    result = predict_diabetes(image_path)
    print("Prediction:", result)