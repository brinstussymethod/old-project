import threading

text = """When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his
eleventy-first birthday with a party of special magnificence, there was much talk and
excitement in Hobbiton. Bilbo was very rich and very peculiar, and had been the wonder of
the Shire for sixty years, ever since his remarkable disappearance and unexpected return.
The riches he had brought back from his travels had now become a local legend, and it was
popularly believed, whatever the old folk might say, that the Hill at Bag End was full of
tunnels stuffed with treasure. And if that was not enough for fame, there was also his
prolonged vigour to marvel at. Time wore on, but it seemed to have little effect on Mr.
Baggins. At ninety he was much the same as at fifty. At ninety-nine they began to call him
well-preserved; but unchanged would have been nearer the mark. There were some that
shook their heads and thought this was too much of a good thing; it seemed unfair that
anyone should possess (apparently) perpetual youth as well as (reputedly) inexhaustible
wealth."It will have to be paid for," they said. "It isn"t natural, and trouble will come of it!"""

# Step 1: Split the text into words
words = text.split()

# Function to find words starting with 'A' or 'a'
def findWordsWithA():
    words_with_a = [word for word in words if word.startswith(('A', 'a'))]
    print("Words starting with 'A' or 'a':", words_with_a)

# Function to find words starting with 'L' or 'l'
def findWordsWithL():
    words_with_l = [word for word in words if word.startswith(('L', 'l'))]
    print("Words starting with 'L' or 'l':", words_with_l)

# Step 2: Create two threads
thread_a = threading.Thread(target=findWordsWithA)
thread_l = threading.Thread(target=findWordsWithL)

# Step 3: Start the threads
thread_a.start()
thread_l.start()

# Step 4: Wait for both threads to complete
thread_a.join()
thread_l.join()