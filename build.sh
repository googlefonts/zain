# Roman
fontmake -u Source/2-Production/Zain_ExtraLight.ufo.zip -o ttf --output-path Fonts/TTF/Zain-ExtraLight.ttf
fontmake -u Source/2-Production/Zain_Light.ufo.zip -o ttf --output-path Fonts/TTF/Zain-Light.ttf
fontmake -u Source/2-Production/Zain_Regular.ufo.zip -o ttf --output-path Fonts/TTF/Zain-Regular.ttf
fontmake -u Source/2-Production/Zain_Bold.ufo.zip -o ttf --output-path Fonts/TTF/Zain-Bold.ttf
fontmake -u Source/2-Production/Zain_ExtraBold.ufo.zip -o ttf --output-path Fonts/TTF/Zain-ExtraBold.ttf
fontmake -u Source/2-Production/Zain_Black.ufo.zip -o ttf --output-path Fonts/TTF/Zain-Black.ttf

# Italic
fontmake -u Source/2-Production/Zain_Italic.ufo.zip -o ttf --output-path Fonts/TTF/ZainItalic-Regular.ttf
python Scripts/rewire_italic.py Fonts/TTF/ZainItalic-Regular.ttf

# After-Burner
for file in Fonts/TTF/*.ttf; do
    python Scripts/fix.py $file

    ttfautohint $file $file.hinted
    mv $file.hinted $file

    gftools fix-hinting $file
    mv $file.fix $file
done
