# Rule-Based Expert System to suggest learning style

#This function asks the user a yes/no question and returns True if the answer is "yes"
def get_input(question):
    answer = input(question + " (yes/no): ").strip().lower()
    return answer == "yes"
#This function determines the user's learning style based on their answers
def determine_learning_style():
    print("Answer the questions below to find your learning style:")
     # Ask questions to check user preferences
    visual = get_input("Do you prefer pictures, diagrams, or visual explanations?")
    auditory = get_input("Do you remember things better when you hear them?")
    kinesthetic = get_input("Do you learn best by doing things yourself?")

    # Rules to decide the learning style
    if visual and not auditory and not kinesthetic:
        return "Visual"
    elif auditory and not visual and not kinesthetic:
        return "Auditory"
    elif kinesthetic and not visual and not auditory:
        return "Kinesthetic"
    elif visual and auditory:
        return "Visual-Auditory"
    elif auditory and kinesthetic:
        return "Auditory-Kinesthetic"
    elif visual and kinesthetic:
        return "Visual-Kinesthetic"
    else:
        return "Mixed" # If user selects all or none, suggest a mixed learning style

#This function suggests learning methods based on the detected learning style
def suggest_learning_methods(style):
    print("\nYour learning style is:", style)
    print("Here are some learning methods for you:")

    if style == "Visual":
        print("- Use diagrams, charts, videos, and mind maps.")
    elif style == "Auditory":
        print("- Listen to podcasts, lectures, or read out loud.")
    elif style == "Kinesthetic":
        print("- Do practical tasks, use hands-on activities and models.")
    elif style == "Visual-Auditory":
        print("- Watch videos with explanations or narrated slides.")
    elif style == "Auditory-Kinesthetic":
        print("- Try doing tasks while listening to instructions.")
    elif style == "Visual-Kinesthetic":
        print("- Use visual materials while doing the activity.")
    else:
        print("- Try a mix of different methods and see what works best.")

# This is the main part of the program that runs everything
if __name__ == "__main__":
    # First , find out the user's learning style
    style = determine_learning_style()
    # Then , suggest suitable learning materials
    suggest_learning_methods(style)
