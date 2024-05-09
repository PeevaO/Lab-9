function addCompany() {
    let compName = document.getElementById('comp_name').value
    let term = document.getElementById('term').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'comp_name': compName,
                             'term': term})
    })

}