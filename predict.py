from simpletransformers.question_answering import QuestionAnsweringModel

modelType = "bert"
modelName = "bert-base-cased"

def predictAnswer(contextString, question):

    response = ""

    toPredict = [
        {
            "qas": [
                {
                    "question": question,
                    "id": "0001",
                }
            ],
            "context": contextString,
        }
    ]

    model = QuestionAnsweringModel("bert", "outputs/bert", use_cuda=False)
    answers, probabs = model.predict(toPredict)

    if answers[0]["answer"][0] == "empty":
        response = "Could not evaluate the answer to this question. Please try again."
        return response

    elif len(answers[0]["answer"]) == 1 and (answers[0]["answer"][0] == ""):
        response = "Could not evaluate the answer to this question. Please try again."
        return response

    else:
        response = answers[0]["answer"][0]
        return response

    return response


ques = "How old is Kanishk?"

cont = "Meet a boy named Kanishk, a 20-year-old young man residing in Chandigarh's Sector 37-D. He has been pursuing his undergraduate in Computer Science Engineering studies at CCET Degree Wing in Sector 26, Chandigarh since 2021. Before joining college, he was a student at Vivek High School in Sector 38-B. Kanishk is passionate about playing football and is an enthusiastic athlete. He even received the Best Athlete (Boys) award during his 10th-grade, which was two years ago, before he started his college journey."


if __name__ == "__main__":
    response = predictAnswer(contextString=cont, question=ques)
    print(response)
