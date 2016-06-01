#Sophie

Version 0.0 (23rd May 2016)</br>
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

(27th May 2016) - Architecture Updates </br>
0.0.5 - Architectural Revision-concept of superbots and bots, bot anywhere in pipeline, new flow diagrams in notebook</br>
0.0.6 - Resolving the parse issue with expressions in 0.0.4 -longest prefix matching and multiple parses, best parses are learnt on the job - through a maintained cache.</br>
0.0.7 - Detailing a few bots to form part of the core infrastructure.</br>
0.0.8 - Bot API detailing </br>

(3rd June 2015) - Pipeline construction </br>
0.0.9 - Keyboard input/output on PC interface</br>
0.0.10 - Decision tree implementation </br>
0.0.11 - Basic bots implementation and testing
0.0.12 - Parser adaptation for new entities and intents </br>
0.0.13 - Pipeline organization - Core Sophie code </br>

Version 0.1 (5th June 2016) - First tangible product </br>

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
             



