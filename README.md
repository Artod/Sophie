# Sophie
A highly-customizable and modular personal assistant bot.

Version 0.1 (23/5/2016) </br>
0.11 - TIME intents added </br>
0.12 - Basic intent parser with highlighting </br>
     - Parsing is slow, since we manually traverse all </br>
       rules to find how to read the intents.
     - Need to develop an automatic LALR parser which optimizes the matches. </br>
     - Plus, the parsing should account for various parsings,
       breakfast can be either a food or timing. We need to put both 
       meanings in a stack and check if the sentence means anything for both. </br>
0.13 - Simple tokenizer implementation for integers and floats(numbers) </br>
0.14 - Longest prefix matching implemented </br>
     - Note now that we have issues with actual parsing </br>
     - 4 times 4 times 4 : will not parse as a single number </br>
     - should we evaluate this expression here?
       or should we somehow accumulate this and evaluate later </br>
     - note our notion of evaluation is do with the intent type only
       can help later on - think of it as a tokenizer-parser separation </br>
     - we will perhaps need the notion of a CSG </br>

