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
    print(type(course_credits)) #Need to make sure that the credits are being stored as an integer, not a string.
    return course_record

def main():
    #Test 1, cleaning up the example transcript and printing the results
    test_transcript = ( "    MTH-111, Pre-calculus, 4, COMPLETED    ",
    "  WR-121z, Composition I, 3, Completed   ",
    "  WR-122z,  Composition II, 3, Incomplete   ",
    "     GSWS-210, Violence Prevention, 4, completed")
    for course in test_transcript:
        result = parse_course_record(course)
        print(result)
    

main()