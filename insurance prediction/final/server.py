from flask import Flask, request, render_template
import pickle

# Load the model
with open('insurance_prediction.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get the values entered by the user
        policy_tenure = float(request.args.get("policy_tenure"))
        age_car = float(request.args.get("age_car"))
        age_policyholder = float(request.args.get("age_policyholder"))
        area_cluster = float(request.args.get("area_cluster"))
        population_density = float(request.args.get("population_density"))
        make = float(request.args.get("make"))
        segment = float(request.args.get("segment"))
        fuel_type = float(request.args.get("fuel_type"))
        engine_type = float(request.args.get("engine_type"))
        airbags = float(request.args.get("airbags"))
        is_esc = float(request.args.get("is_esc"))
        is_adjustable_steering = float(request.args.get("is_adjustable_steering"))
        is_tpms = float(request.args.get("is_tpms"))
        is_parking_sensors = float(request.args.get("is_parking_sensors"))
        is_parking_camera = float(request.args.get("is_parking_camera"))
        rear_brakes_type = float(request.args.get("rear_brakes_type"))
        displacement = float(request.args.get("displacement"))
        cylinder = float(request.args.get("cylinder"))
        transmission_type = float(request.args.get("transmission_type"))
        gear_box = float(request.args.get("gear_box"))
        steering_type = float(request.args.get("steering_type"))
        turning_radius = float(request.args.get("turning_radius"))
        Length = float(request.args.get("Length"))
        height = float(request.args.get("height"))
        Gross_weight = float(request.args.get("Gross_weight"))
        is_front_fog_lights = float(request.args.get("is_front_fog_lights"))
        is_rear_window_wiper = float(request.args.get("is_rear_window_wiper"))
        is_rear_window_washer = float(request.args.get("is_rear_window_washer"))
        is_rear_window_defogger = float(request.args.get("is_rear_window_defogger"))
        is_brake_assist = float(request.args.get("is_brake_assist"))
        is_power_door_locks = float(request.args.get("is_power_door_locks"))
        is_central_locking = float(request.args.get("is_central_locking"))
        is_power_steering = float(request.args.get("is_power_steering"))
        is_driver_seat_height_adjustable = float(request.args.get("is_driver_seat_height_adjustable"))
        is_day_night_rear_view_mirror = float(request.args.get("is_day_night_rear_view_mirror"))
        is_ecw = float(request.args.get("is_ecw"))
        is_speed_alert = float(request.args.get("is_speed_alert"))
        ncap_rating = float(request.args.get("ncap_rating"))
        x1 = 1
        x2 = 1
        x3 = 1
        x4 = 1
        x5 = 1
        x6 = 1
        x7 = 1
        x8 = 1
        x9 = 1
        x10 = 1
        x11 = 1
        x12 = 1
        x13 = 1
        x14 = 1
        x15 = 1
        x16 = 1
        x17 = 1
        x18 = 1
        x19 = 1
        x20 = 1
        x21 = 1
        x22 = 1
        x23 = 1
        x24 = 1
        x25 = 1
        x26 = 1
        x27 = 1
        x28 = 1
        x29 = 1
        x30 = 1
        x31 = 1
        x32 = 1
        x33 = 1
        x34 = 1
        x35 = 1
        x36 = 1
        x37 = 1
        x38 = 1
        x39 = 1
        x40 = 1
        x41 = 1
        x42 = 1
        x43 = 1
        x44 = 1
        x45 = 1
        x46 = 1
        x47 = 1
        x48 = 1
        x49 = 1
        x50 = 1
        x51 = 1
        x52 = 1
        x53 = 1
        x54 = 1
        x55 = 1
        x56 = 1
        x57 = 1
        x58 = 1
        x59 = 1

        # Make prediction using the loaded model
        prediction = model.predict([[policy_tenure, age_car, age_policyholder, area_cluster, population_density, make,
                                     segment, fuel_type, engine_type, airbags, is_esc, is_adjustable_steering, is_tpms,
                                     is_parking_sensors, is_parking_camera, rear_brakes_type, displacement, cylinder,
                                     transmission_type, gear_box, steering_type, turning_radius, Length, height,
                                     Gross_weight, is_front_fog_lights, is_rear_window_wiper, is_rear_window_washer,
                                     is_rear_window_defogger, is_brake_assist, is_power_door_locks, is_central_locking,
                                     is_power_steering, is_driver_seat_height_adjustable, is_day_night_rear_view_mirror,
                                     is_ecw, is_speed_alert, ncap_rating, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11
                                     , x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26,
                                     x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40,
                                     x41, x42, x43, x44, x45, x46, x47, x48, x49, x50,
                                     x51, x52, x53, x54, x55, x56, x57, x58, x59]])

        if prediction[0] == 1:
            result = "The vehicle won't opt for insurance in the near future."
        else:
            result = "The vehicle will opt for insurance in the near future."

        return render_template('result.html', result=result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
