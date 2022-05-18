# mal_on_tokens_and_types

Python scripts for Chinese texts processing and application of the Menzerath-Altmann law
________________________________________________________________________________________

The scripts were created for a small project which tests the Menzerath-Altmann law on Chinese word tokens and types.

The Menzerath-Altmann law, one of the well-known laws from the field of quantitative linguistics, describes a relationship between particular (not necessarily) language units:

"The longer a language construct, the shorter its components (constituents)" (Altmann, 1980, p. 124),
or even more generally:
"The length of the components is a function of the length of language constructs" (Altmann, 1980, p. 125).

We tested the menzerathian relationship between the Chinese word (tokens and types) being the construct and various units being its constituents and sub-constituent, resulting in four different triplets of language units:

a) the word measured in syllables (constituents) and the syllable measured in its phonemes (sub-constituents),
b) the word measured in syllables (constituents) and the syllable measured in its pinyin letters (sub-constituents),
c) the word measured in Chinese characters (constituents) and the character measured in its components (sub-constituents),
d) the word measured in Chinese characters (constituents) and the character measured in its strokes (sub-constituents).

The python scripts process a language material, in our case Chinese texts written in pinyin and Chinese characters, and quantify the word lengths according to the units of measurement mentioned above.

Data input:
We opted for two Chinese translations of the New Testament (the 27-book canon) published online by the International Biblical Association as a part of the Wordproject® (available at https://www.wordproject.org/). The first version, 'Sheng Jing: Xinyue Quan Shu', is captured in pinyin transcription (available at https://www.wordproject.org/bibles/pn/index.htm), while the second 圣经：新约全书 is written in simplified Chinese characters (available at https://www.wordproject.org/bibles/gb_cat/index.htm). The New Testament written in pinyin was used for testing the a and b triplets and the version in Chinese characters for the c and d triplets.

Data output:
By using the scripts and the data input above, we created four datasets that allowed us to further proceed with the application of the law (i.e., to extract all categories of word lengths, their frequencies, and mean constituent lengths and to fit these data with mathematical models of the law):

1) new_testament_40_66_pinyin_token -> word lengths in syllables, phonemes, and pinyin letters for the tokens (a and b),
2) new_testament_40_66_pinyin_type -> word lengths in syllables, phonemes and pinyin letters for the types (a and b),
3) new_testament_40_66_character_token -> word lengths in characters, components and strokes for the tokens (c and d),
4) new_testament_40_66_character_type -> word lengths in characters, components and strokes for the types (c and d).

The fitting results are available at [TBA].