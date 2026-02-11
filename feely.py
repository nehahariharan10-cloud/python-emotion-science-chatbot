import random 
chatCount = 0

# Keywords
happyFeeling =  ["happy", "excited", "content", "joyful", "cheerful", "optimistic", "relieved", "playful", "satisfied", "grateful"]
sadFeeling = ["sad", "lonely", "disappointed", "hopeless", "melancholic", "downcast", "tearful", "empty", "regretful", "heartbroken"]
angryFeeling =  ["angry", "frustrated", "irritated", "resentful", "annoyed", "furious", "hostile", "bitter", "impatient", "agitated"]
scaredFeeling =  ["anxious", "nervous", "worried", "overwhelmed", "uneasy", "tense", "restless", "fearful", "insecure", "panicked"]
feelingsList = [happyFeeling, sadFeeling, angryFeeling, scaredFeeling]

# Responses
happyResponses = ["When you feel this way, your brain is likely releasing dopamine and serotonin, which support motivation, reward, and emotional balance. This often happens when you feel safe, connected, or are making progress.", "This mood reflects increased activity in the brain's reward system. Factors like sunlight, movement, rest, and positive social interaction can strengthen this state.", "Your nervous system appears regulated, with lower stress hormones. Positive emotions often arise when the brain perceives stability, achievement, or belonging."]
sadResponses =  ["This emotional state is often linked to lower dopamine and serotonin activity, which can reduce energy and motivation. It may be influenced by loss, fatigue, or prolonged stress.", "When sadness is present, the brain may be processing emotional meaning or change. Reflection and memory-related regions tend to be more active during this state.", "External factors such as poor sleep, routine disruption, or feeling unsupported can shape this mood. It is often a signal that the brain needs rest or care."]
angryResponses = ["Anger is associated with increased activity in the amygdala, the brain's threat-detection system. It commonly appears when boundaries feel crossed or goals are blocked.", "Stress hormones like cortisol and adrenaline can intensify this response. Lack of sleep or feeling unheard can reduce impulse regulation.", "This state reflects the brain prioritizing protection and control. Anger often signals perceived unfairness or overload rather than a character flaw."]
scaredResponses = ["Anxiety is driven by heightened activity in fear and prediction circuits in the brain. The nervous system may be preparing for potential threats.", "This state is influenced by uncertainty, overstimulation, caffeine, or sleep deprivation. The brain shifts toward vigilance over calm.", "When anxiety appears, the stress response is active. Predictability, reassurance, and grounding can help the brain return to regulation."]
randomResponses = ["That sounds emotionally layered.", "Your brain might still be sorting it out.", "Your mood may be influenced by multiple factors working at once."]

# feelingsList > emotion > feeling 
def findFeeling(userText):
    for word in userText: # checks each word the user has in their input
        if word in happyFeeling:
            return "happy"
        if word in sadFeeling:
            return "sad"
        if word in angryFeeling:
            return "angry"
        if word in scaredFeeling:
            return "scared"
                
while True:
    chatCount += 1
    if chatCount == 1:
        print("Hello, I'm Feely!")
        print("I'm an AI bot that teaches you about the science behind your feelings.")
        print("(Say \"bye\" to quit)")
        print("")
        userResponse = input("How are you feeling today?   ") 
    else:
        print ("")
        userResponse = input("Tell me another feeling you're noticing:   ")
    
    if userResponse == "bye":
        break
    
    response_to_list = userResponse.split()
    print("")
    
    if findFeeling(response_to_list) == "happy":
        print("(^_^)   " + random.choice(happyResponses))
    elif findFeeling(response_to_list) == "sad":
        print("(._.)   " + random.choice(sadResponses))
    elif findFeeling(response_to_list) == "angry":
        print("(ಠ_ಠ)" + random.choice (angryResponses))
    elif findFeeling(response_to_list) == "scared":
        print("(•_•;)   " + random.choice(scaredResponses))
    else: # findFeeling didn't return anything
        print("(~_~)   " + random.choice(randomResponses))
        
        

# exit message
print("")
print("Goodbye!")
print("")
print("( •_•)")
print("<)   )╯")
print(" |   |")