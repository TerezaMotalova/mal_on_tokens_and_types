# mal_on_tokens_and_types

Python scripts for Chinese texts processing and application of the Menzerath-Altmann law
________________________________________________________________________________________

The scripts were created for a small project which tests the Menzerath-Altmann law on Chinese word tokens and types.

The Menzerath-Altmann law, one of the well-known laws from the field of quantitative linguistics, describes a relationship between particular (not necessarily) language units:

> *"The longer a language construct, the shorter its components (constituents)"* (Altmann, 1980, p. 124),

or even more generally:

> *"The length of the components is a function of the length of language constructs"* (Altmann, 1980, p. 125).

We tested the menzerathian relationship between the Chinese word (tokens and types) being the construct and various units being its constituents and sub-constituent, resulting in four different triplets of language units:

+ a == the word measured in syllables (constituents) and the syllable measured in its phonemes (sub-constituents),
+ b == the word measured in syllables (constituents) and the syllable measured in its pinyin letters (sub-constituents),
+ c == the word measured in Chinese characters (constituents) and the character measured in its components (sub-constituents),
+ d == the word measured in Chinese characters (constituents) and the character measured in its strokes (sub-constituents).

The python scripts process a language material, in our case Chinese texts written in pinyin and Chinese characters, and quantify the word lengths according to the units of measurement mentioned above.

Data input:
We opted for two Chinese translations of the New Testament (the 27-book canon) published online by the International Biblical Association as a part of the [Wordproject®] (available at https://www.wordproject.org/). The first version, ['Sheng Jing: Xinyue Quan Shu'](https://www.wordproject.org/bibles/pn/index.htm), is captured in pinyin transcription, while the second [圣经：新约全书](https://www.wordproject.org/bibles/gb_cat/index.htm) is written in simplified Chinese characters. The New Testament written in pinyin was used for testing the a and b triplets and the version in Chinese characters for the c and d triplets.

Data output:
By using the scripts and the data input above, we created four datasets that allowed us to further proceed with the application of the law (i.e., to extract all categories of word lengths, their frequencies, and mean constituent lengths and to fit these data with mathematical models of the law):

1. new_testament_40_66_pinyin_token -> word lengths in syllables, phonemes, and pinyin letters for the tokens (a and b),
2. new_testament_40_66_pinyin_type -> word lengths in syllables, phonemes and pinyin letters for the types (a and b),
3. new_testament_40_66_character_token -> word lengths in characters, components and strokes for the tokens (c and d),
4. new_testament_40_66_character_type -> word lengths in characters, components and strokes for the types (c and d).

The fitting results are available at TBA.

Persistent identifier of the repository (scripts and data):
<a href="https://zenodo.org/badge/latestdoi/493632778"><img src="https://zenodo.org/badge/493632778.svg" alt="DOI"></a>

License of the repository (scripts and data)::
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="http://10.5281/zenodo.8003699">The Menzerath-Altmann Law on tokens and types</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/TerezaMotalova">Tereza Motalova</a> is marked with <a href="http://creativecommons.org/publicdomain/zero/1.0?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC0 1.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/zero.svg?ref=chooser-v1"></a></p>