import datetime

__author__ = 'Desmond'

import csv

i = 0
filename = 'admin_download_surveys.csv'

survey_1_eligible_count = 0
survey_2_eligible_count = 0
survey_3_eligible_count = 0
survey_4_eligible_count = 0
survey_5_eligible_count = 0
survey_1_eligible_intervention_count = 0
survey_2_eligible_intervention_count = 0
survey_3_eligible_intervention_count = 0
survey_4_eligible_intervention_count = 0
survey_5_eligible_intervention_count = 0
survey_1_eligible_control_count = 0
survey_2_eligible_control_count = 0
survey_3_eligible_control_count = 0
survey_4_eligible_control_count = 0
survey_5_eligible_control_count = 0
survey_1_completed_count = 0
survey_2_completed_count = 0
survey_3_completed_count = 0
survey_4_completed_count = 0
survey_5_completed_count = 0
survey_1_completed_intervention_count = 0
survey_2_completed_intervention_count = 0
survey_3_completed_intervention_count = 0
survey_4_completed_intervention_count = 0
survey_5_completed_intervention_count = 0
survey_1_completed_control_count = 0
survey_2_completed_control_count = 0
survey_3_completed_control_count = 0
survey_4_completed_control_count = 0
survey_5_completed_control_count = 0
survey_1_incomplete_eligible_count = 0
survey_2_incomplete_eligible_count = 0
survey_3_incomplete_eligible_count = 0
survey_4_incomplete_eligible_count = 0
survey_5_incomplete_eligible_count = 0
survey_1_incomplete_intervention_count = 0
survey_2_incomplete_intervention_count = 0
survey_3_incomplete_intervention_count = 0
survey_4_incomplete_intervention_count = 0
survey_5_incomplete_intervention_count = 0
survey_1_incomplete_control_count = 0
survey_2_incomplete_control_count = 0
survey_3_incomplete_control_count = 0
survey_4_incomplete_control_count = 0
survey_5_incomplete_control_count = 0
survey_1_incomplete_overdue_less = 0
survey_2_incomplete_overdue_less = 0
survey_3_incomplete_overdue_less = 0
survey_4_incomplete_overdue_less = 0
survey_5_incomplete_overdue_less = 0
survey_1_incomplete_overdue_greater = 0
survey_2_incomplete_overdue_greater = 0
survey_3_incomplete_overdue_greater = 0
survey_4_incomplete_overdue_greater = 0
survey_5_incomplete_overdue_greater = 0
survey_1_moved_eligible_count = 0
survey_2_moved_eligible_count = 0
survey_3_moved_eligible_count = 0
survey_4_moved_eligible_count = 0
survey_5_moved_eligible_count = 0
survey_1_moved_intervention_count = 0
survey_2_moved_intervention_count = 0
survey_3_moved_intervention_count = 0
survey_4_moved_intervention_count = 0
survey_5_moved_intervention_count = 0
survey_1_moved_control_count = 0
survey_2_moved_control_count = 0
survey_3_moved_control_count = 0
survey_4_moved_control_count = 0
survey_5_moved_control_count = 0

with open(filename) as surveys:
    reader = csv.reader(surveys)
    csv_list = list(reader)

    for line in csv_list[1:]:

        print("LIST ENTRY: ", line[0])
        user_id = line[0]
        arm = line[1]
        name = line[2]
        gender = line[3]
        last_contact = line[4]
        survey_1 = line[5]
        survey_2 = line[6]
        survey_3 = line[7]
        survey_4 = line[8]
        survey_5 = line[9]
        next_survey = line[10]
        next_survey_due = line[11]
        phone = line[12]
        email = line[13]
        address = line[14]
        city = line[15]
        state = line[16]
        zip = line[17]

        print(user_id, ',', arm, ',', name, ',', gender, ',', last_contact, ',', survey_1, ','
              , survey_2, ',', survey_3, ',', survey_4, ',', survey_5, ',', next_survey, ','
              , next_survey_due, ',', phone, ',', email, ',', address, ',', city, ',', state, ',', zip)

        today = datetime.date.today()
        print("TODAY: ", today)
        print("NEXT SURVEY DUE", next_survey_due, '\n')

        if next_survey_due == "":
            print("Null next survey due", '\n')

        else:
            split = next_survey_due.split('/')
            print("NEXT SURVEY DUE SPLIT: ", split)
            next_survey_converted = datetime.date(int(split[2]), int(split[0]), int(split[1]))

            print("CONVERTED DATETIME NEXT SURVEY: ", next_survey_converted.toordinal())
            print("TODAY: ", today.toordinal())
            print("NEXT SURVEY: ", next_survey)
            survey_1_eligible = (int(next_survey) > 1) or (int(next_survey) == 1 and
                                                           int(next_survey_converted.toordinal())
                                                           < int(today.toordinal()))
            if survey_1_eligible:
                survey_1_eligible_count += 1

            survey_2_eligible = (int(next_survey) > 2) or (int(next_survey) == 2 and
                                                           int(next_survey_converted.toordinal())
                                                           < int(today.toordinal()))
            if survey_2_eligible:
                print("FOUND SURVEY 2 ELIGIBLE", survey_2_eligible, '\n')
                survey_2_eligible_count += 1
                print("SURVEY 2 ELIGIBLE:", survey_2_eligible)

            survey_3_eligible = (int(next_survey) > 3) or (int(next_survey) == 3 and
                                                           int(next_survey_converted.toordinal())
                                                           < int(today.toordinal()))
            if survey_3_eligible:
                print("FOUND SURVEY 3 ELIGIBLE", survey_3_eligible, '\n')
                survey_3_eligible_count += 1
                print("SURVEY 3 ELIGIBLE:", survey_3_eligible)

            survey_4_eligible = (int(next_survey) > 4) or (int(next_survey) == 4 and
                                                           int(next_survey_converted.toordinal())
                                                           < int(today.toordinal()))
            if survey_4_eligible:
                print("FOUND SURVEY 4 ELIGIBLE", survey_4_eligible, '\n')
                survey_4_eligible_count += 1
                print("SURVEY 4 ELIGIBLE:", survey_4_eligible)

            survey_5_eligible = (int(next_survey) > 5) or (int(next_survey) == 5 and
                                                           int(next_survey_converted.toordinal())
                                                           < int(today.toordinal()))
            if survey_5_eligible:
                print("FOUND SURVEY 5 ELIGIBLE", survey_5_eligible, '\n')
                survey_5_eligible_count += 1
                print("SURVEY 5 ELIGIBLE:", survey_5_eligible)

            survey_1_eligible_intervention = survey_1_eligible and (arm == "INTERVENTION")
            if survey_1_eligible_intervention:
                print("FOUND SURVEY 1 ELIGIBLE INTERVENTION", survey_1_eligible_intervention)
                survey_1_eligible_intervention_count += 1

            survey_2_eligible_intervention = survey_2_eligible and (arm == "INTERVENTION")
            if survey_2_eligible_intervention:
                print("FOUND SURVEY 2 ELIGIBLE INTERVENTION", survey_2_eligible_intervention)
                survey_2_eligible_intervention_count += 1

            survey_3_eligible_intervention = survey_3_eligible and (arm == "INTERVENTION")
            if survey_3_eligible_intervention:
                print("FOUND SURVEY 3 ELIGIBLE INTERVENTION", survey_3_eligible_intervention)
                survey_3_eligible_intervention_count += 1

            survey_4_eligible_intervention = survey_4_eligible and (arm == "INTERVENTION")
            if survey_4_eligible_intervention:
                print("FOUND SURVEY 4 ELIGIBLE INTERVENTION", survey_4_eligible_intervention)
                survey_4_eligible_intervention_count += 1

            survey_5_eligible_intervention = survey_5_eligible and (arm == "INTERVENTION")
            if survey_5_eligible_intervention:
                print("FOUND SURVEY 5 ELIGIBLE INTERVENTION", survey_5_eligible_intervention, '\n')
                survey_5_eligible_intervention_count += 1

            survey_1_eligible_control = survey_1_eligible and (arm == "CONTROL")
            if survey_1_eligible_control:
                print("FOUND SURVEY 1 ELIGIBLE CONTROL", survey_1_eligible_control)
                survey_1_eligible_control_count += 1

            survey_2_eligible_control = survey_2_eligible and (arm == "CONTROL")
            if survey_2_eligible_control:
                print("FOUND SURVEY 2 ELIGIBLE CONTROL", survey_2_eligible_control)
                survey_2_eligible_control_count += 1

            survey_3_eligible_control = survey_3_eligible and (arm == "CONTROL")
            if survey_3_eligible_control:
                print("FOUND SURVEY 3 ELIGIBLE CONTROL", survey_3_eligible_control)
                survey_3_eligible_control_count += 1

            survey_4_eligible_control = survey_4_eligible and (arm == "CONTROL")
            if survey_4_eligible_control:
                print("FOUND SURVEY 4 ELIGIBLE CONTROL", survey_4_eligible_control)
                survey_4_eligible_control_count += 1

            survey_5_eligible_control = survey_5_eligible and (arm == "CONTROL")
            if survey_5_eligible_control:
                print("FOUND SURVEY 5 ELIGIBLE CONTROL", survey_5_eligible_control, '\n')
                survey_5_eligible_control_count += 1

            survey_1_completed = survey_1_eligible and (survey_1.__contains__("Completed "))
            if survey_1_completed:
                print("FOUND SURVEY 1 COMPLETED", survey_1_completed)
                survey_1_completed_count += 1

            survey_2_completed = survey_2_eligible and (survey_2.__contains__("Completed "))
            if survey_2_completed:
                print("FOUND SURVEY 2 COMPLETED", survey_2_completed)
                survey_2_completed_count += 1

            survey_3_completed = survey_3_eligible and (survey_3.__contains__("Completed "))
            if survey_3_completed:
                print("FOUND SURVEY 3 COMPLETED", survey_3_completed)
                survey_3_completed_count += 1

            survey_4_completed = survey_4_eligible and (survey_4.__contains__("Completed "))
            if survey_4_completed:
                print("FOUND SURVEY 4 COMPLETED", survey_4_completed)
                survey_4_completed_count += 1

            survey_5_completed = survey_5_eligible and (survey_5.__contains__("Completed "))
            if survey_5_completed:
                print("FOUND SURVEY 5 COMPLETED", survey_5_completed, '\n')
                survey_5_completed_count += 1

            survey_1_completed_intervention = survey_1_completed and (arm == "INTERVENTION")
            if survey_1_completed_intervention:
                print("FOUND SURVEY 1 COMPLETED INTERVENTION ", survey_1_completed_intervention)
                survey_1_completed_intervention_count += 1

            survey_2_completed_intervention = survey_2_completed and (arm == "INTERVENTION")
            if survey_2_completed_intervention:
                print("FOUND SURVEY 2 COMPLETED INTERVENTION ", survey_2_completed_intervention)
                survey_2_completed_intervention_count += 1

            survey_3_completed_intervention = survey_3_completed and (arm == "INTERVENTION")
            if survey_3_completed_intervention:
                print("FOUND SURVEY 3 COMPLETED INTERVENTION ", survey_3_completed_intervention)
                survey_3_completed_intervention_count += 1

            survey_4_completed_intervention = survey_4_completed and (arm == "INTERVENTION")
            if survey_4_completed_intervention:
                print("FOUND SURVEY 4 COMPLETED INTERVENTION ", survey_4_completed_intervention)
                survey_4_completed_intervention_count += 1

            survey_5_completed_intervention = survey_5_completed and (arm == "INTERVENTION")
            if survey_5_completed_intervention:
                print("FOUND SURVEY 5 COMPLETED INTERVENTION ", survey_5_completed_intervention, '\n')
                survey_5_completed_intervention_count += 1

            survey_1_completed_control = survey_1_completed and (arm == "CONTROL")
            if survey_1_completed_control:
                print("FOUND SURVEY 1 COMPLETED CONTROL ", survey_1_completed_control)
                survey_1_completed_control_count += 1

            survey_2_completed_control = survey_2_completed and (arm == "CONTROL")
            if survey_2_completed_control:
                survey_2_completed_control = survey_2_completed and (arm == "CONTROL")
                print("FOUND SURVEY 2 COMPLETED CONTROL ", survey_2_completed_control)
                survey_2_completed_control_count += 1

            survey_3_completed_control = survey_3_completed and (arm == "CONTROL")
            if survey_3_completed_control:
                print("FOUND SURVEY 3 COMPLETED CONTROL ", survey_3_completed_control)
                survey_3_completed_control_count += 1

            survey_4_completed_control = survey_4_completed and (arm == "CONTROL")
            if survey_4_completed_control:
                print("FOUND SURVEY 4 COMPLETED CONTROL ", survey_4_completed_control)
                survey_4_completed_control_count += 1

            survey_5_completed_control = survey_5_completed and (arm == "CONTROL")
            if survey_5_completed_control:
                print("FOUND SURVEY 5 COMPLETED CONTROL ", survey_5_completed_control, '\n')
                survey_5_completed_control_count += 1

            survey_1_incomplete_eligible = survey_1_eligible and (not survey_1.__contains__("Completed "))
            if survey_1_incomplete_eligible:
                print("FOUND SURVEY 1 INCOMPLETE ELIGIBLE ", survey_1_incomplete_eligible)
                survey_1_incomplete_eligible_count += 1

            survey_2_incomplete_eligible = survey_1_eligible and (not survey_2.__contains__("Completed "))
            if survey_2_incomplete_eligible:
                print("FOUND SURVEY 2 INCOMPLETE ELIGIBLE ", survey_2_incomplete_eligible)
                survey_2_incomplete_eligible_count += 1

            survey_3_incomplete_eligible = survey_1_eligible and (not survey_3.__contains__("Completed "))
            if survey_3_incomplete_eligible:
                print("FOUND SURVEY 3 INCOMPLETE ELIGIBLE ", survey_3_incomplete_eligible)
                survey_3_incomplete_eligible_count += 1

            survey_4_incomplete_eligible = survey_1_eligible and (not survey_4.__contains__("Completed "))
            if survey_4_incomplete_eligible:
                print("FOUND SURVEY 4 INCOMPLETE ELIGIBLE ", survey_4_incomplete_eligible)
                survey_4_incomplete_eligible_count += 1

            survey_5_incomplete_eligible = survey_1_eligible and (not survey_5.__contains__("Completed "))
            if survey_5_incomplete_eligible:
                print("FOUND SURVEY 5 INCOMPLETE ELIGIBLE ", survey_5_incomplete_eligible, '\n')
                survey_5_incomplete_eligible_count += 1

            survey_1_incomplete_intervention = survey_1_incomplete_eligible and (arm == "INTERVENTION")
            if survey_1_incomplete_intervention:
                print("FOUND SURVEY 1 INCOMPLETE INTERVENTION ", survey_1_incomplete_intervention)
                survey_1_incomplete_intervention_count += 1

            survey_2_incomplete_intervention = survey_2_incomplete_eligible and (arm == "INTERVENTION")
            if survey_2_incomplete_intervention:
                print("FOUND SURVEY 2 INCOMPLETE INTERVENTION ", survey_2_incomplete_intervention)
                survey_2_incomplete_intervention_count += 1

            survey_3_incomplete_intervention = survey_3_incomplete_eligible and (arm == "INTERVENTION")
            if survey_3_incomplete_intervention:
                print("FOUND SURVEY 3 INCOMPLETE INTERVENTION ", survey_3_incomplete_intervention)
                survey_3_incomplete_intervention_count += 1

            survey_4_incomplete_intervention = survey_4_incomplete_eligible and (arm == "INTERVENTION")
            if survey_4_incomplete_intervention:
                print("FOUND SURVEY 4 INCOMPLETE INTERVENTION ", survey_4_incomplete_intervention)
                survey_4_incomplete_intervention_count += 1

            survey_5_incomplete_intervention = survey_5_incomplete_eligible and (arm == "INTERVENTION")
            if survey_5_incomplete_intervention:
                print("FOUND SURVEY 5 INCOMPLETE INTERVENTION ", survey_5_incomplete_intervention, '\n')
                survey_5_incomplete_intervention_count += 1

            survey_1_incomplete_control = survey_1_incomplete_eligible and (arm == "CONTROL")
            if survey_1_incomplete_control:
                print("FOUND SURVEY 1 INCOMPLETE CONTROL ", survey_1_incomplete_control)
                survey_1_incomplete_control_count += 1

            survey_2_incomplete_control = survey_2_incomplete_eligible and (arm == "CONTROL")
            if survey_2_incomplete_control:
                print("FOUND SURVEY 2 INCOMPLETE CONTROL ", survey_2_incomplete_control)
                survey_2_incomplete_control_count += 1

            survey_3_incomplete_control = survey_3_incomplete_eligible and (arm == "CONTROL")
            if survey_3_incomplete_control:
                print("FOUND SURVEY 3 INCOMPLETE CONTROL ", survey_3_incomplete_control)
                survey_3_incomplete_control_count += 1

            survey_4_incomplete_control = survey_4_incomplete_eligible and (arm == "CONTROL")
            if survey_4_incomplete_control:
                print("FOUND SURVEY 4 INCOMPLETE CONTROL ", survey_4_incomplete_control)
                survey_4_incomplete_control_count += 1

            survey_5_incomplete_control = survey_5_incomplete_eligible and (arm == "CONTROL")
            if survey_5_incomplete_control:
                print("FOUND SURVEY 5 INCOMPLETE CONTROL ", survey_5_incomplete_control, '\n')
                survey_5_incomplete_control_count += 1

            weeks = datetime.timedelta(604800 * 3)
            three_weeks = datetime.datetime(1, 1, 1) + weeks

            survey_1_overdue_less = survey_1_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                      < today.toordinal() - three_weeks.toordinal())
            if survey_1_overdue_less:
                print("FOUND SURVEY 1 OVERDUE LESS THAN 3 WEEKS", survey_1_overdue_less)
                survey_1_incomplete_overdue_less += 1

            survey_2_overdue_less = survey_2_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                      < today.toordinal() - three_weeks.toordinal())
            if survey_2_overdue_less:
                print("FOUND SURVEY 2 OVERDUE LESS THAN 3 WEEKS", survey_2_overdue_less)
                survey_2_incomplete_overdue_less += 1

            survey_3_overdue_less = survey_3_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                      < today.toordinal() - three_weeks.toordinal())
            if survey_3_overdue_less:
                print("FOUND SURVEY 3 OVERDUE LESS THAN 3 WEEKS", survey_3_overdue_less)
                survey_3_incomplete_overdue_less += 1

            survey_4_overdue_less = survey_4_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                      < today.toordinal() - three_weeks.toordinal())
            if survey_4_overdue_less:
                print("FOUND SURVEY 4 OVERDUE LESS THAN 3 WEEKS", survey_4_overdue_less)
                survey_4_incomplete_overdue_less += 1

            survey_5_overdue_less = survey_5_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                      < today.toordinal() - three_weeks.toordinal())
            if survey_5_overdue_less:
                print("FOUND SURVEY 5 OVERDUE LESS THAN 3 WEEKS", survey_5_overdue_less)
                survey_5_incomplete_overdue_less += 1

            survey_1_overdue_greater = survey_1_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                         >= today.toordinal() - three_weeks.toordinal())
            if survey_1_overdue_greater:
                print("FOUND SURVEY 1 OVERDUE GREATER THAN 3 WEEKS", survey_1_overdue_greater)
                survey_1_incomplete_overdue_greater += 1

            survey_2_overdue_greater = survey_2_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                         >= today.toordinal() - three_weeks.toordinal())
            if survey_2_overdue_greater:
                print("FOUND SURVEY 2 OVERDUE GREATER THAN 3 WEEKS", survey_2_overdue_greater)
                survey_2_incomplete_overdue_greater += 1

            survey_3_overdue_greater = survey_3_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                         >= today.toordinal() - three_weeks.toordinal())
            if survey_3_overdue_less:
                print("FOUND SURVEY 3 OVERDUE GREATER THAN 3 WEEKS", survey_3_overdue_greater)
                survey_3_incomplete_overdue_greater += 1

            survey_4_overdue_greater = survey_4_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                         >= today.toordinal() - three_weeks.toordinal())
            if survey_4_overdue_greater:
                print("FOUND SURVEY 4 OVERDUE GREATER THAN 3 WEEKS", survey_4_overdue_greater)
                survey_4_incomplete_overdue_greater += 1

            survey_5_overdue_greater = survey_5_incomplete_eligible and (int(next_survey_converted.toordinal())
                                                                         >= today.toordinal() - three_weeks.toordinal())
            if survey_5_overdue_greater:
                print("FOUND SURVEY 5 OVERDUE GREATER THAN 3 WEEKS", survey_5_overdue_greater)
                survey_5_incomplete_overdue_greater += 1

            survey_1_moved_eligible = survey_1_eligible and (survey_1.__contains__("missed "))
            if survey_1_moved_eligible:
                print("FOUND SURVEY 1 MOVED ELIGIBLE ", survey_1_moved_eligible, '\n')
                survey_1_moved_eligible_count += 1

            survey_2_moved_eligible = survey_2_eligible and (survey_2.__contains__("missed "))
            if survey_2_moved_eligible:
                print("FOUND SURVEY 2 MOVED ELIGIBLE ", survey_2_moved_eligible, '\n')
                survey_2_moved_eligible_count += 1

            survey_3_moved_eligible = survey_3_eligible and (survey_3.__contains__("missed "))
            if survey_3_moved_eligible:
                print("FOUND SURVEY 3 MOVED ELIGIBLE ", survey_3_moved_eligible, '\n')
                survey_3_moved_eligible_count += 1

            survey_4_moved_eligible = survey_4_eligible and (survey_4.__contains__("missed "))
            if survey_4_moved_eligible:
                print("FOUND SURVEY 4 MOVED ELIGIBLE ", survey_4_moved_eligible, '\n')
                survey_4_moved_eligible_count += 1

            survey_5_moved_eligible = survey_5_eligible and (survey_5.__contains__("missed "))
            if survey_5_moved_eligible:
                print("FOUND SURVEY 5 MOVED ELIGIBLE ", survey_5_moved_eligible, '\n')
                survey_5_moved_eligible_count += 1

            survey_1_moved_intervention = survey_1_moved_eligible and (arm == "INTERVENTION")
            if survey_1_moved_intervention:
                print("FOUND SURVEY 1 MOVED INTERVENTION", survey_1_moved_intervention)
                survey_1_moved_intervention_count += 1

            survey_2_moved_intervention = survey_2_moved_eligible and (arm == "INTERVENTION")
            if survey_2_moved_intervention:
                print("FOUND SURVEY 2 MOVED INTERVENTION", survey_2_moved_intervention)
                survey_2_moved_intervention_count += 1

            survey_3_moved_intervention = survey_3_moved_eligible and (arm == "INTERVENTION")
            if survey_3_moved_intervention:
                print("FOUND SURVEY 3 MOVED INTERVENTION", survey_3_moved_intervention)
                survey_3_moved_intervention_count += 1

            survey_4_moved_intervention = survey_4_moved_eligible and (arm == "INTERVENTION")
            if survey_4_moved_intervention:
                print("FOUND SURVEY 4 MOVED INTERVENTION", survey_4_moved_intervention)
                survey_4_moved_intervention_count += 1

            survey_5_moved_intervention = survey_5_moved_eligible and (arm == "INTERVENTION")
            if survey_5_moved_intervention:
                print("FOUND SURVEY 5 MOVED INTERVENTION", survey_5_moved_intervention, '\n')
                survey_5_moved_intervention_count += 1

            survey_1_moved_control = survey_1_moved_eligible and (arm == "CONTROL")
            if survey_1_moved_control:
                print("FOUND SURVEY 1 MOVED CONTROL", survey_1_moved_control)
                survey_1_moved_control_count += 1

            survey_2_moved_control = survey_2_moved_eligible and (arm == "CONTROL")
            if survey_2_moved_control:
                print("FOUND SURVEY 2 MOVED CONTROL", survey_2_moved_control)
                survey_2_moved_control_count += 1

            survey_3_moved_control = survey_3_moved_eligible and (arm == "CONTROL")
            if survey_3_moved_control:
                print("FOUND SURVEY 3 MOVED CONTROL", survey_3_moved_control)
                survey_3_moved_control_count += 1

            survey_4_moved_control = survey_4_moved_eligible and (arm == "CONTROL")
            if survey_4_moved_control:
                print("FOUND SURVEY 4 MOVED CONTROL", survey_4_moved_control)
                survey_4_moved_control_count += 1

            survey_5_moved_control = survey_5_moved_eligible and (arm == "CONTROL")
            if survey_5_moved_control:
                print("FOUND SURVEY 5 MOVED CONTROL", survey_5_moved_control, '\n')
                survey_5_moved_control_count += 1

print("SURVEY 1 ELIGIBLE: ", survey_1_eligible_count)
print("SURVEY 1 ELIGIBLE INTERVENTION: ", survey_1_eligible_intervention_count)
print("SURVEY 1 ELIGIBLE CONTROL: ", survey_1_eligible_control_count)
print("SURVEY 1 COMPLETED ELIGIBLE: ", survey_1_completed_count)
print("SURVEY 1 COMPLETED INTERVENTION: ", survey_1_completed_intervention_count)
print("SURVEY 1 COMPLETED CONTROL: ", survey_1_completed_control_count)
print("SURVEY 1 INCOMPLETE ELIGIBLE: ", survey_1_incomplete_eligible_count)
print("SURVEY 1 INCOMPLETE INTERVENTION: ", survey_1_incomplete_intervention_count)
print("SURVEY 1 INCOMPLETE CONTROL: ", survey_1_incomplete_control_count)
print("SURVEY 1 OVERDUE LESS THAN 3 WEEKS", survey_1_incomplete_overdue_less)
print("SURVEY 1 OVERDUE GREATER THAN 3 WEEKS", survey_1_incomplete_overdue_greater)
print("SURVEY 1 MOVED ELIGIBLE: ", survey_1_moved_eligible_count)
print("SURVEY 1 MOVED INTERVENTION: ", survey_1_moved_intervention_count)
print("SURVEY 1 MOVED CONTROL: ", survey_1_moved_control_count, '\n')

print("SURVEY 2 ELIGIBLE: ", survey_2_eligible_count)
print("SURVEY 2 ELIGIBLE INTERVENTION: ", survey_2_eligible_intervention_count)
print("SURVEY 2 ELIGIBLE CONTROL: ", survey_2_eligible_control_count)
print("SURVEY 2 COMPLETED ELIGIBLE: ", survey_2_completed_count)
print("SURVEY 2 COMPLETED INTERVENTION: ", survey_2_completed_intervention_count)
print("SURVEY 2 COMPLETED CONTROL: ", survey_2_completed_control_count)
print("SURVEY 2 INCOMPLETE ELIGIBLE: ", survey_2_incomplete_eligible_count)
print("SURVEY 2 INCOMPLETE INTERVENTION: ", survey_2_incomplete_intervention_count)
print("SURVEY 2 INCOMPLETE CONTROL: ", survey_2_incomplete_control_count)
print("SURVEY 2 OVERDUE LESS THAN 3 WEEKS", survey_2_incomplete_overdue_less)
print("SURVEY 2 OVERDUE GREATER THAN 3 WEEKS", survey_2_incomplete_overdue_greater)
print("SURVEY 2 MOVED ELIGIBLE: ", survey_2_moved_eligible_count)
print("SURVEY 2 MOVED INTERVENTION: ", survey_2_moved_intervention_count)
print("SURVEY 2 MOVED CONTROL: ", survey_2_moved_control_count, '\n')

print("SURVEY 3 ELIGIBLE: ", survey_3_eligible_count)
print("SURVEY 3 ELIGIBLE INTERVENTION: ", survey_3_eligible_intervention_count)
print("SURVEY 3 ELIGIBLE CONTROL: ", survey_3_eligible_control_count)
print("SURVEY 3 COMPLETED ELIGIBLE: ", survey_3_completed_count)
print("SURVEY 3 COMPLETED INTERVENTION: ", survey_3_completed_intervention_count)
print("SURVEY 3 COMPLETED CONTROL: ", survey_3_completed_control_count)
print("SURVEY 3 INCOMPLETE ELIGIBLE: ", survey_3_incomplete_eligible_count)
print("SURVEY 3 INCOMPLETE INTERVENTION: ", survey_3_incomplete_intervention_count)
print("SURVEY 3 INCOMPLETE CONTROL: ", survey_3_incomplete_control_count)
print("SURVEY 3 OVERDUE LESS THAN 3 WEEKS", survey_3_incomplete_overdue_less)
print("SURVEY 3 OVERDUE GREATER THAN 3 WEEKS", survey_3_incomplete_overdue_greater)
print("SURVEY 3 MOVED ELIGIBLE: ", survey_3_moved_eligible_count)
print("SURVEY 3 MOVED INTERVENTION: ", survey_3_moved_intervention_count)
print("SURVEY 3 MOVED CONTROL: ", survey_3_moved_control_count, '\n')

print("SURVEY 4 ELIGIBLE: ", survey_4_eligible_count)
print("SURVEY 4 ELIGIBLE INTERVENTION: ", survey_4_eligible_intervention_count)
print("SURVEY 4 ELIGIBLE CONTROL: ", survey_4_eligible_control_count)
print("SURVEY 4 COMPLETED ELIGIBLE: ", survey_4_completed_count)
print("SURVEY 4 COMPLETED INTERVENTION: ", survey_4_completed_intervention_count)
print("SURVEY 4 COMPLETED CONTROL: ", survey_4_completed_control_count)
print("SURVEY 4 INCOMPLETE ELIGIBLE: ", survey_4_incomplete_eligible_count)
print("SURVEY 4 INCOMPLETE INTERVENTION: ", survey_4_incomplete_intervention_count)
print("SURVEY 4 INCOMPLETE CONTROL: ", survey_4_incomplete_control_count)
print("SURVEY 4 OVERDUE LESS THAN 3 WEEKS", survey_4_incomplete_overdue_less)
print("SURVEY 4 OVERDUE GREATER THAN 3 WEEKS", survey_4_incomplete_overdue_greater)
print("SURVEY 4 MOVED ELIGIBLE: ", survey_4_moved_eligible_count)
print("SURVEY 4 MOVED INTERVENTION: ", survey_4_moved_intervention_count)
print("SURVEY 4 MOVED CONTROL: ", survey_4_moved_control_count, '\n')

print("SURVEY 5 ELIGIBLE: ", survey_5_eligible_count)
print("SURVEY 5 ELIGIBLE INTERVENTION: ", survey_5_eligible_intervention_count)
print("SURVEY 5 ELIGIBLE CONTROL: ", survey_5_eligible_control_count)
print("SURVEY 5 COMPLETED ELIGIBLE: ", survey_5_completed_count)
print("SURVEY 5 COMPLETED INTERVENTION: ", survey_5_completed_intervention_count)
print("SURVEY 5 COMPLETED CONTROL: ", survey_5_completed_control_count)
print("SURVEY 5 INCOMPLETE ELIGIBLE: ", survey_5_incomplete_eligible_count)
print("SURVEY 5 INCOMPLETE INTERVENTION: ", survey_5_incomplete_intervention_count)
print("SURVEY 5 INCOMPLETE CONTROL: ", survey_5_incomplete_control_count)
print("SURVEY 5 OVERDUE LESS THAN 3 WEEKS", survey_5_incomplete_overdue_less)
print("SURVEY 5 OVERDUE GREATER THAN 3 WEEKS", survey_5_incomplete_overdue_greater)
print("SURVEY 5 MOVED ELIGIBLE: ", survey_5_moved_eligible_count)
print("SURVEY 5 MOVED INTERVENTION: ", survey_5_moved_intervention_count)
print("SURVEY 5 MOVED CONTROL: ", survey_5_moved_control_count, '\n')

print("3 WEEKS CONVERSION", three_weeks.toordinal())