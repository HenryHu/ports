--- Telegram/SourceFiles/history/history_inner_widget.cpp.orig	2018-02-06 06:24:24 UTC
+++ Telegram/SourceFiles/history/history_inner_widget.cpp
@@ -1187,16 +1187,16 @@ void HistoryInner::mouseActionFinish(con
 	_widget->noSelectingScroll();
 	_widget->updateTopBarSelection();
 
-#if defined Q_OS_LINUX32 || defined Q_OS_LINUX64
+#if defined Q_OS_LINUX32 || defined Q_OS_LINUX64 || defined Q_OS_FREEBSD
 	if (!_selected.empty() && _selected.cbegin()->second != FullSelection) {
 		const auto [item, selection] = *_selected.cbegin();
		if (const auto view = item->mainView()) {
			SetClipboardWithEntities(
				view->selectedText(selection),
				QClipboard::Selection);
		}
 	}
-#endif // Q_OS_LINUX32 || Q_OS_LINUX64
+#endif // Q_OS_LINUX32 || Q_OS_LINUX64 || Q_OS_FREEBSD
 }
 
 void HistoryInner::mouseReleaseEvent(QMouseEvent *e) {
