# Sophie
A highly-customizable and modular personal assistant bot.

Version 0.1 (23/5/2016) </br>
0.11 - TIME intents added </br>
0.12 - Basic intent parser with highlighting </br>
     - Parsing is slow, since we manually traverse all </br>
       rules to find how to read the intents. </br>
     - Need to develop an automatic LALR parser which optimizes the matches. </br>
     - Plus, the parsing should account for various parsings, </br>
       breakfast can be either a food or timing. We need to put both </br>
       meanings in a stack and check if the sentence means anything for both. </br>
0.13 - Simple tokenizer implementation for integers and floats(numbers) </br>
0.14 - Longest prefix matching implemented </br>

