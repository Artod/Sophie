#Sophie

Version 0.0 (23rd May 2015)
0.0.1 - TIME intents added
0.0.2 - Basic intent parser with highlighting
     - Parsing is slow, since we manually traverse all
       rules to find how to read the intents.
     - Need to develop an automatic LALR parser which optimizes the matches.
     - Plus, the parsing should account for various parsings,
       breakfast can be either a food or timing. We need to put both
       meanings in a stack and check if the sentence means anything for both.
0.0.3 - Simple tokenizer implementation for integers and floats(numbers)
0.0.4 - Longest prefix matching implemented
     - Note now that we have issues with actual parsing
     - 4 times 4 times 4 : will not parse as a single number
     - should we evaluate this expression here?
       or should we somehow accumulate this and evaluate later
     - note our notion of evaluation is do with the intent type only
       can help later on - think of it as a tokenizer-parser separation
     - we will perhaps need the notion of a CSG

(24th May 2015) - Architecture Updates
0.0.5 - Architectural Revision    
0.0.6 - Resolving the parse issue with expressions in 0.0.4
0.0.7 - Detailing further INTENTS
0.0.8 - Describing IO interface - develop basic input and output modules

(25th May 2015) - Modularization and Model Selection
0.0.9 - Modularize the whole pipeline as per decided architecture
0.0.10 - Selection of language generation models/ML/NLP/DM models to provide for bot building

Version 0.1 (26th May 2015) - First tangible product
0.1 - Formal revision of entire pipeline. Should be ready to use with a couple of basic bots - ContactsBot and PropertyBot.
0.1.1 - Basic Bot planning.

To do
-----
Intents - CLR parser for intent matching
        - Intent implementation
        - Intent learning architecture
        - Failsafe for incorrect intent recognition
        - Comprehensive list of basic intents
        - Where to evaluate intents
        
IO interface - Sticky screen (have to save state probably)
             - Lists/Dropdowns/Autocomplete/Buttons
             - Spell check (probably a good idea to correct before it is fed in)
             - Colour and font library
             - Load screen
             - Plan for more GUI elements (Tree/Table)
             - Lightweight OpenGL context to draw all these (consider a high-level library like SDL)
             
Models - Selection of a language generation model
       - Training data
       - Hooking to response module
       - Testing syntactic and semantic correctness
       - Implementation/selection of ML/AI/FL models
       
Bot interface API - Clear definition of how bots must be implemented, time constraints on query to bot, hint to prune this bot
Dynamic program generation
NaturallySophie scripting language
             



