import datetime as dt
while True:
    try:
        yourQuestion = input("Hãy nhập câu hỏi của bạn (Nếu như bạn muốn dừng thì hãy nhập bye hoặc tạm biệt hoặc tắt): ")
        if "mấy giờ" in yourQuestion or "hôm nay" in yourQuestion:
            today_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(today_date)
        elif "học" in yourQuestion and "nên" in yourQuestion:
            print("Bạn đang phân vân về vấn đề học tập của bạn, bạn hãy nên ưu tiên cho việc học của bạn \n" \
            "Nếu như bạn đang bệnh thì hãy cho tôi biết")
            yourAnswer = input("Tình trạng sức khỏe của bạn: ")
            if "bệnh" in yourAnswer:
                print("Bạn hãy nghỉ ngơi để khỏe lại rồi học, có sức khỏe mới có thể học tốt được")
            else:
                print("Bạn nên học cố gắng lên nhé")
            del yourAnswer
        elif "bye" in yourQuestion or "tạm biệt" in yourQuestion or "tắt" in yourQuestion:
            break
    except:
        print("Lỗi hãy nhập lại")
del yourQuestion

