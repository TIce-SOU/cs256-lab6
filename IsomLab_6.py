#Anthony Isom, Lab 6, creating a algorithm that will "processes a student's course history—represented as a tuple of raw, unformatted text strings—and sorts their completed courses into designated General Education (Gen Ed) category bins. "

def parse_course_record(course_string):  #part 1, cleans string and puts into a dictionary
    '''Parse_course_record breaks up the provided transcripts from a string into a dictionary with multiple keys
    Parameter: 
    Course_string(string): The courses taken within the transcript

    Return: 
    A dictionary with the string split up in the “keys: 'code', 'name', 'credits', and 'status'.''' 

    #cleaning string based on return format above. Making sure each part is consitent, and credits is stored as an integer. 
    course_parts = course_string.split(", ")
    course_code = course_parts[0].strip().upper()
    course_name = course_parts[1].strip().title()
    course_credits = int(course_parts[2].strip())
    course_status = course_parts[3].strip().lower()

    course_record = {
        'code': course_code,
        'name': course_name,
        'credits': course_credits,
        'status': course_status
    }
    #print(type(course_credits)) #Need to make sure that the credits are being stored as an integer, not a string.
    return course_record

def get_gen_ed_category(course_code, gen_ed_mapping): #part 2, finds the category of the course based on the mapping provided. If not found, returns Uncategorized.
    '''get_gen_ed_category determines what the course provides applies to within the Gen ED requirements.

    Parameters: 
    course_code(string): The course main ID code to locate whether it applies to the requirements or not
    gen_ed_mapping(dictionary): Based on the input, returns the values associated or Uncategorized

    Return: The category associated with the string or Uncategorized'''

    for category, courses in gen_ed_mapping.items():
        if course_code in courses:
            return category
        else: continue
    return "Uncategorized"
#finds courses within category, and if not found, returns Uncategorized.

def audit_credits(student_bins): #part 3, calculates the total amount of completed credits from Gen ED. Specifically lists the completed credits per category.
    '''audit_credits calculates the total amount of completed credits from Gen ED. Specifically lists the completed credits per category.

    Parameter:
    Student_bins(dict): This separates the categorical names(keys) within Gen ED and assigns the total amount for each category (starting at 0).

    Return:
    A dictionary containing the Gen ED keys (categorized and uncategorized), and the values of the total amount of completed credits'''
    credit_count = {}

    for category in student_bins:
        credit_count[category] = 0 #default value for each category is 0

    for category, courses in student_bins.items():
        for course_code, credits in courses:
            credit_count[category] += credits

    return credit_count

def bin_student_course(transcript, gen_ed_mapping): #part 4, creates a dictionary where the keys for Gen ED keys are the categories and the values are the tuples (code, credits)
    '''bin_student_course creates a dictionary where the keys for Gen ED keys are the categories and the values are the tuples (code, credits)

    Parameter:
    transcript(string): A long string containing the class name, code, and credits
    gen_ed_mapping(dictionary): This is used to map the string to each category. 
    
    Return:
    A dictionary with the keys being the Gen ED category and the values are tuples containing the class code and credits.'''

    student_bins = {}
    for category in gen_ed_mapping:
        student_bins[category] = []
    student_bins["Uncategorized"] = []

    for course_string in transcript: #Processing each course in the transcript, parsing it, and then checking if it is completed. If completed, it will be categorized and added to the student_bins dictionary.
        course = parse_course_record(course_string)
        course_code = course['code']
        course_credits = course['credits']
        course_status = course['status']
        if course_status == "completed":
            category = get_gen_ed_category(course_code, gen_ed_mapping)
            student_bins[category].append((course_code, course_credits))

    return student_bins

def main():
    #Test 1, cleaning up the example transcript and printing the results
    #test_transcript = ( "    MTH-111, Pre-calculus, 4, COMPLETED    ",
    #"  WR-121z, Composition I, 3, Completed   ",
    #"  WR-122z,  Composition II, 3, Incomplete   ",
    #"     GSWS-210, Violence Prevention, 4, completed")
    #for course in test_transcript:
        #result = parse_course_record(course)
        #print(result)
    
    #Test 2, categorizing the courses based on the Gen Ed mapping
    gen_ed_mapping = {
       # "Creativity and Innovation": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
        #"Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"]
    }
    #print(f"Code: ART-133 \nCategory: {get_gen_ed_category('ART-133', gen_ed_mapping)} \n")
    #print(f"Code: GSWS-210 \nCategory: {get_gen_ed_category('GSWS-210', gen_ed_mapping)} \n")
    #print(f"Code: ARTH-204 \nCategory: {get_gen_ed_category('ARTH-204', gen_ed_mapping)} \n")
    #print(f"Code: MTH-111 \nCategory: {get_gen_ed_category('MTH-111', gen_ed_mapping)} \n")

    #Test 3, auditing the credits based on the Gen Ed mapping and the completed courses
    #student_bins =  {
        #"Numerical Literacy": [ ("CS-200", 4),("MTH-111", 4)],
        #"Inquiry and Analysis": [ ("ENG-280", 4), ("BI-101", 2)],
        #"Uncategorized": [("ES-103", 3), ("ES-103 Lab", 0)]
    #}
    #total_credits = audit_credits(student_bins)
    #print(total_credits)

    #Test 4, binning the student courses based on the Gen Ed mapping from previous test and the completed courses
    #student_transcript = ("HONS-256, Honors Probability and Statistics, 4, completed", "CS-256, Computer Science 2, 4, completed", "ART-133, Art Appreciation, 4, completed", "ARTH-204, Art History 1, 4, completed")
    #student_bins = bin_student_course(student_transcript, gen_ed_mapping)
    #print("Student Course Bins:")
    #print(student_bins)

    # Test 5, running the entire process with a sample transcript and Gen Ed mapping
    gen_ed_categories = {
        "Communication and Expression": [
            "ARTH-204",
            "BA-450"
        ],
        "Creativity and Innovation": [
            "ART-133",
            "ART-291"
        ],
        "Equity, Diversity, and Inclusion": [
            "ARTH-450",
            "ENG-214"
        ],
        "Inquiry and Analysis": [
            "GSWS-300",
            "ES-200",
            "HST-201Z"
        ],
        "Numerical Literacy": [
            "CS-200",
            "MTH-111Z",
            "MTH-112Z"
        ],
        "Purposeful Learning": [
            "WR-121Z",
            "WR-122Z"
        ]
    }
    Transcript = (
        "   MTH-111z, Pre-Calculus 1: Functions,  4, Completed  ",
        "   MTH-112Z, pre-calculus 2: trigonometry, 4, completed   ", #2 courses I have completed in one category (Numerical Literacy)
        "  ART-133, Art appreciation, 4, completed   ", #Creativity and Innovation
        "  WR-121z, composition 1, 4, Completed  ", #Purposeful Learning
        " HST-201z, United States History 1, 4, completed   ", #Inquiry and Analysis
        "   ENG-214, Ethics: Moral Issues, 4, COMPLETED  ", #Equity, Diversity, and Inclusion
        "    ES-327, Energy and Climate Change, 4, Incompleted    ", #Communication and Expression, incompleted
        " BA-450, Using GIS in Buisness, 4, completed ", #Communication and Expression
        " ES-494, Env. Science/Policy Capstone 1, 4, completed ", #Class thats uncategorized, not in the Gen Ed mapping
    )



    student_final_bins = bin_student_course(Transcript, gen_ed_categories)
    print(f"Student Course Bins: \n{student_final_bins}\n " )
    #organizing the completed courses into their respective categories, and if not found, into Uncategorized.

    credit_totals = audit_credits(student_final_bins)
    print(f"Total Completed Credits by Category: \n{credit_totals}\n " )
    #Calculating the total amount of completed credits from Gen ED. Specifically lists the completed credits per category.

    overall_credits = sum(credit_totals.values())
    print(f"\nOverall Completed Credits: {overall_credits}")

main()