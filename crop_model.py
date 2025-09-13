# model/crop_model.py

def get_advice(input_data, is_image=False):
    if is_image:
        return "Detected disease from photo. Apply neem spray and water daily."
    else:
        text = input_data.lower()
        if "pest" in text:
            return "Pest detected. Use natural pesticides and monitor crops."
        elif "yellow" in text:
            return "Leaves turning yellow. Check soil nutrients and water properly."
        else:
            return "Crop looks healthy. Follow regular care."