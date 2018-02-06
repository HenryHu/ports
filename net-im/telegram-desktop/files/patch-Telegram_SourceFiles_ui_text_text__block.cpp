--- Telegram/SourceFiles/ui/text/text_block.cpp.orig	2018-01-03 10:46:01 UTC
+++ Telegram/SourceFiles/ui/text/text_block.cpp
@@ -320,6 +320,9 @@ TextBlock::TextBlock(const style::font &
 
 		QStackTextEngine engine(part, blockFont->f);
 		BlockParser parser(&engine, this, minResizeWidth, _from, part);
+		QTextLayout layout(part, blockFont->f);
+		layout.beginLayout();
+		layout.createLine();
 
 		CrashReports::ClearAnnotationRef("CrashString");
 	}
