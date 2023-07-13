from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    #"I'm interested in all patients who have never changed practice, between these two dates"
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

    age  = patients.age_as_of(
        "2019-09-01", #"Give me a column of data corresponding to the age of each patient on the given date"
        
        #"I expect every patient to have a value, and the distribution of ages to match that of the real UK population"
        return_expectations = {
            "rate" : "universal",
            "int": {"distribution": "population_ages"},
        }
    )



)


