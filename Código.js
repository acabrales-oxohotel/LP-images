function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index')
      .setTitle('Celebra Amor y Amistad con OxoHotel')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
