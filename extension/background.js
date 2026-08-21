chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "check-rbi-guidance",
    title: "Check against RBI Guidance",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "check-rbi-guidance" && info.selectionText) {
    chrome.storage.local.set({ pendingQuery: info.selectionText }, () => {
      chrome.action.openPopup();
    });
  }
});
