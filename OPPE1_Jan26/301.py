def total_engagement(video: dict) -> int:
# Returns the total engagement (likes + comments) for a given video.
    total = int( video["likes"])+int(video["comments"])
    return total

def engagement_rate(video: dict) -> float:
# Returns the engagement rate for a given video, using the formula:
#                    likes + comments
# Engagement Rate = ------------------  x 100
#                         views
# If views is 0, return 0.0
# Round the result to 2 decimal places

    likes = video["likes"]
    comments = video["comments"]
    views = video["views"]
    if views == 0:
        return 0.0
    else:
        return round(((likes+comments)/views)*100,2)


def most_engaging_video(videos: list[dict]) -> str:
# Returns the title of the video with the highest engagement rate. If there is a tie, return the first one in the list.
    lst = []
    highest = 0
    for i in videos:
        engagement = 0
        for j in i:
            likes = j["likes"]
            comments = j["comments"]
            views = j["views"]
            if views == 0:
                engagement = 0.0
            else:
                engagement = round(((likes+comments)/views)*100,2)
        if engagement>=highest:
            highest = engagement
            lst.append(j["title"])
        
    return lst[0]

def videos_with_engagement_rate_above_threshold(videos: list[dict], threshold: float) -> list[str]:
    lst = []
    # highest = 0
    for i in videos:
        engagement = 0
        for j in i:
            likes = j["likes"]
            comments = j["comments"]
            views = j["views"]
            if views == 0:
                engagement = 0.0
            else:
                engagement = round(((likes+comments)/views)*100,2)
        if engagement>threshold:
            # highest = engagement
            lst.append(j["title"])
        
    return lst

def average_engagement_rate(videos: list[dict]) -> float:
    total = 0
    countwithnotzero = 0
    for i in videos:
        engagement = 0
        for j in i:
            likes = j["likes"]
            comments = j["comments"]
            views = j["views"]
            if views == 0:
                engagement = 0.0
            else:
                engagement = round(((likes+comments)/views)*100,2)
                total+=engagement
                countwithnotzero +=1
    average = total/countwithnotzero
    return average
