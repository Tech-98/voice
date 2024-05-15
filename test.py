from db import pyannote_db
import os

test_directory = r"test_data/"
train_directory = r"train_data/"
directory = r"saif/"
passed = 0
failed = 0

manal_obj = pyannote_db(train_directory+ "manal.wav")
ben_obj = pyannote_db(train_directory+ "ben.wav")
saif_obj = pyannote_db(train_directory+ "saif.wav")
cian_obj = pyannote_db(train_directory+ "cian.wav")
shaheer_obj = pyannote_db(train_directory+ "shaheer.wav")

for name in os.listdir(test_directory+directory):
    # Open file
    with open(os.path.join(test_directory+directory, name)) as f:
        # print(f"Content of '{name}'")
        try:
            name, distance =pyannote_db.get_closest_distance(str(test_directory+directory+name))
            print(name, str(distance) )
            if distance < 0.5 and name == directory.split("/")[0]:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print("Error: ",e)
            continue
print(f"Passed: {passed}/ {passed+failed}, Failed: {failed}/ {passed+failed}")
print(f"Accuracy: {round(passed/(passed+failed)*100,2)}%")