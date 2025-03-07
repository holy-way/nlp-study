Studying From https://wikidocs.net/217238

# Cleaning and Normalization 

* Cleaning : Cleaning noise data from corpus
* Normalization : Unify various forms of word into same word

Cleaning is conducted before and after tokenization.   
It can be done through the projects.

# 1. Unifying words based on rules - (normalization)
ex)
* USA = US
* uh-huh = uhhuh

# 2. Unifying upper and lower case - (normalization)
* Positive Case
	* Automobile = automobile
In general cases, converting into lower cases helps normalization.

* Negative Case
	* US != us
	* (United States) != we, us
There are some cases, where upper case word have different meaning from lower case word.    
Names of companies and people should be maintained as upper case word.    

* Use Cases
	* Set rules when not to convert
	* Converting all to lower case might be useful

# 3. Deleting not useful words - (cleaning)

* 1. Rarely appearing words
The words appearing rarely would not be helpful.

* 2. Short words
	* English words are usually 6~7 letters.
	* Deleting words under 2 letters might be helpful.
		* 1 letter - a, I
		* 2 letters - it, at, to, on, in, by

# 4. Regular Expression - (cleaning)
Regular expressions are used to delete repetitive and not useful words.   
ex) 
* Newspaper content - upload time
* HTML Document - HTML Tag