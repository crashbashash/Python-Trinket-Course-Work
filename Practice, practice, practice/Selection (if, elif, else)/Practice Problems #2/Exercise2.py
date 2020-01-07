try:
    eng_results = int(input("What are your English results?: "))
    math_results = int(input("What are your Maths results?: "))

    if eng_results > 50 and math_results > 50:
        print("Your English and Maths results are very good")
    elif eng_results < 50 and math_results > 50:
        print("Your Maths is very good")
    elif eng_results > 50 and math_results < 50:
        print("Your English is very good")
    else:
        print("You need to revice your Maths and English")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")