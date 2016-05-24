#Sophie

Version 0.0 (23rd May 2015) </br>
0.0.1 - TIME intents added </br>
0.0.2 - Basic intent parser with highlighting </br>
     - Parsing is slow, since we manually traverse all
       rules to find how to read the intents. </br>
     - Need to develop an automatic LALR parser which optimizes the matches. </br>
     - Plus, the parsing should account for various parsings,
       breakfast can be either a food or timing. We need to put both
       meanings in a stack and check if the sentence means anything for both. </br>
0.0.3 - Simple tokenizer implementation for integers and floats(numbers) </br>
0.0.4 - Longest prefix matching implemented
     - Note now that we have issues with actual parsing </br>
     - 4 times 4 times 4 : will not parse as a single number </br>
     - should we evaluate this expression here? 
       or should we somehow accumulate this and evaluate later </br>
     - note our notion of evaluation is do with the intent type only
       can help later on - think of it as a tokenizer-parser separation </br>
     - we will perhaps need the notion of a CSG </br>

(24th May 2015) - Architecture Updates </br>
0.0.5 - Architectural Revision </br>
0.0.6 - Resolving the parse issue with expressions in 0.0.4 </br>
0.0.7 - Detailing further INTENTS </br>
0.0.8 - Describing IO interface - develop basic input and output modules </br>

(25th May 2015) - Modularization and Model Selection </br>
0.0.9 - Modularize the whole pipeline as per decided architecture </br>
0.0.10 - Selection of language generation models/ML/NLP/DM models to provide for bot building </br>

Version 0.1 (26th May 2015) - First tangible product </br>
0.1 - Formal revision of entire pipeline. Should be ready to use with a couple of basic bots - ContactsBot and PropertyBot. </br>
0.1.1 - Basic Bot planning. </br>

To do</br>
-----</br>
Intents - CLR parser for intent matching </br>
        - Intent implementation </br>
        - Intent learning architecture </br>
        - Failsafe for incorrect intent recognition </br>
        - Comprehensive list of basic intents </br>
        - Where to evaluate intents </br>
        
IO interface - Sticky screen (have to save state probably) </br>
             - Lists/Dropdowns/Autocomplete/Buttons </br>
             - Spell check and autocorrect learning(probably a good idea to correct before it is fed in) </br>
             - Colour and font library </br>
             - Load screen </br>
             - Plan for more GUI elements (Tree/Table) </br>
             - Lightweight OpenGL context to draw all these (consider a high-level library like SDL) </br>
             
Models - Selection of a language generation model </br>
       - Training data </br>
       - Hooking to response module </br>
       - Testing syntactic and semantic correctness </br>
       - Implementation/selection of ML/AI/FL models </br>
       
Bot interface API - Clear definition of how bots must be implemented, time constraints on query to bot, hint to prune this bot </br>
Dynamic program generation </br>
NaturallySophie scripting language </br>
             



