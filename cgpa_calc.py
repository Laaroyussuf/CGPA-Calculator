import pandas as pd
import streamlit as st

grade_equ = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
grade_equ_4 = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

def get_data(grade_system, num_courses):
    units, grades, points = [], [], []

    for i in range(num_courses):
        unit = st.selectbox(f'Course Unit {i+1}', list(range(1, 11)))
        units.append(unit)
        
        if grade_system == 5.0:
            grade = st.selectbox(f'Grade', list(grade_equ.keys()), key=i)
            grades.append(grade)
            points.append(grade_equ[grade])
        else:
            grade = st.selectbox(f'Grade', list(grade_equ_4.keys()), key=i)
            grades.append(grade)
            points.append(grade_equ_4[grade])

    return units, grades, points

def class_5(cgpa):
    if cgpa >= 4.5:
        st.balloons()
        st.success(f'CGPA: {cgpa} First Class')
        return 'Congratulation! You are in First Class.'
    elif 3.5 <= cgpa < 4.5:
        st.success(f'CGPA: {cgpa}')
        return 'Good, you are in Second Class Upper.'
    elif 2.4 <= cgpa < 3.5:
        st.warning(f'CGPA: {cgpa}')
        return 'You are in Second Class Lower.'
    else:
        st.error(f'CGPA: {cgpa}')
        return 'You Pass.'

def class_4(cgpa):
    if cgpa >= 3.5:
        st.balloons()
        st.success(f'CGPA: {cgpa}')
        return 'Congratulation! You are in First Class.'
    elif 3.0 <= cgpa < 3.5:
        st.success(f'CGPA: {cgpa}')
        return 'Good, you are in Second Class Upper.'
    elif 2.0 <= cgpa < 3.0:
        st.warning(f'CGPA: {cgpa}')
        return 'You are in Second Class Lower.'
    else:
        st.error(f'CGPA: {cgpa}')
        return 'You Pass.'

def main():
    st.title('CGPA Calculator')
    img_url = 'https://th.bing.com/th/id/R.c2e6607a1e14b715e4916ff8a40465d7?rik=C3bD4N7Cw2VB1A&pid=ImgRaw&r=0'
    st.image(img_url, use_column_width=True)
    st.markdown(
        'This app calculates your CGPA based on the grading system you select. '
        'Choose your grading system and enter the number of courses you are taking.'
    )
    
    grade_system = st.selectbox('Select Grading System:', [4.0, 5.0])
    num_courses = st.number_input('Number of courses offering:', min_value=1, step=1)
    
    st.write('Fill out the following:')
    
    units, grades, points = get_data(grade_system, num_courses)
    
    if st.button('Calculate GPA'):
        df = pd.DataFrame({'Course Units': units, 'Grades': grades, 'Points': points},
                          index=[i for i in range(1, num_courses + 1)])
        df['Unit_Point'] = df['Course Units'] * df['Points']
        total_unit = df['Course Units'].sum()
        user_total_point = df['Unit_Point'].sum()
        cgpa = round((user_total_point / total_unit), 2)

        st.write('Your GPA breakdown:')
        st.dataframe(df)
        st.write(f'Total Unit: {total_unit}')

        if grade_system == 5.0:
            supposed_total_point = 5 * total_unit
            st.write(f'Your Total point: {user_total_point} out of {supposed_total_point}')
            st.write(class_5(cgpa))
        else:
            supposed_total_point = 4 * total_unit
            st.write(f'Your Total point: {user_total_point} out of {supposed_total_point}')
            st.write(class_4(cgpa))

if __name__ == '__main__':
    main()