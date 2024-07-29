# Zain

The objectives behind ZAIN range of typefaces was to create a unique modern range (7 weights: Extralight, Light, Regular, Regular Italic, Bold, ExtraBold and Black ) that support Arabic
and Latin languages as well as Urdu, Farsi, Kurdish, Indonesian and Tagalog, suitable for headlines, sub-headings and body text, respecting Arabic calligraphy and cultural rules with maximum legibility, 
also and more important is to be in harmony between the Latin and the Arabic and suitable for all communications needs being desktop or digital. 

Source data are from Glyphs:

./Source/1-Drawings/Zain-Black.glyphs
./Source/1-Drawings/Zain-Bold.glyphs
./Source/1-Drawings/Zain-ExtraBold.glyphs
./Source/1-Drawings/Zain-ExtraLight.glyphs
./Source/1-Drawings/Zain-Italic.glyphs
./Source/1-Drawings/Zain-Light.glyphs
./Source/1-Drawings/Zain-LightItalic.glyphs
./Source/1-Drawings/Zain-Regular.glyphs

Glyphs data are used as source file format for the outline design. 

UFO data are used as production file format. The features including the anchorpoints for the marks and base characters are stored in a feature file which is part of the UFO file.

./Source/2-Production /Zain_Black.ufo
./Source/2-Production /Zain_Bold.ufo
./Source/2-Production /Zain_ExtraBold.ufo
./Source/2-Production /Zain_ExtraLight.ufo
./Source/2-Production /Zain_Italic.ufo
./Source/2-Production /Zain_Light.ufo
./Source/2-Production /Zain_LightItalic.ufo
./Source/2-Production /Zain_Regular.ufo


# Build

TTF fonts are currently built using `sh build.sh`, which generates fonts from the `.ufo.zip` sources and runs afterburner scripts over them to make them conform to Google Fonts specs as much as possible.

Because Google Fonts generates webfonts server-side during the onboarding process, I've deleted the webfonts from this repository, but they could be added back again with another step in the build process.
