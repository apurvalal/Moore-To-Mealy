import pandas as pd
import dataframe_image as dfi

def convertor(q1, q1_z, q1_o, q1_output, q2, q2_z, q2_o, q2_output, q3, q3_z, q3_o, q3_output, ):
    current_state = [q1, q2, q3]
    next_state_z = [q1_z, q2_z, q3_z]
    next_state_o = [q1_o, q2_o, q3_o]
    output = [q1_output, q2_output, q3_output]

    moore_dictionary = {q1:q1_output, q2:q2_output, q3:q3_output}
    moore_machine = {"Current State": current_state, "0": next_state_z, "1":next_state_o, "Output":output}

    moore_machine = pd.DataFrame(moore_machine)
    moore_machine.set_index("Current State", inplace=True)

    mealy_string = "{current_state}, {output}"

    mealy_zero = []
    mealy_one = []

    for index in range(0, 3):
        mealy_zero.append(mealy_string.format(current_state=moore_machine['0'][index], output=moore_dictionary[moore_machine['0'][index]]))
        mealy_one.append(mealy_string.format(current_state=moore_machine['1'][index], output=moore_dictionary[moore_machine['1'][index]]))

    mealy_machine = {"Current State": current_state, "0": mealy_zero, "1": mealy_one}

    mealy_machine = pd.DataFrame(mealy_machine)
    mealy_machine.set_index("Current State", inplace=True)

    df_styled = mealy_machine.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(df_styled,"static/mealy_machine.png")
