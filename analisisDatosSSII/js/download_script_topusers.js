    inputNum = document.getQueryVariable("numberline");
    url = "/parte2/usuariosCriticos/downloadPDF"
    url = url + "?numberline=" + inputNum;

    element = document.getElementById('pdfButton');
    element.setAttribute('href', url);