let sortDirection = true;
let header = [
    "broj",
    "datum",
    "posiljalac",
    "porucilac",
    "primalac",
    "artikal",
    "prevoznik",
    "registracija",
    "vozac",
    "bruto",
    "tara",
    "neto",
];
let data = [];
let dates = [];
function createData(reports, date, args) {
    reports.forEach(item => {
        data.push(item)
    });
    
    date.forEach(item => {
        dates.push(item)
    });
    console.log(dates)
    pagination(args)
}
const createTable = (editedData) => {
    let tableBox = document.querySelector('.tbody');
    // let table = document.createElement('table');
    tableBox.innerHTML = '';
                    
    // Cell names
    // let headerRow = document.createElement("tr");
    // header.forEach((text, index) => {
    //     let headerText = document.createElement('th');
    //     // headerText.innerHTML = `<h3>${text}</h3><i class="fas fa-sort-down" style="color: #ff7f50;"></i>`;
    //     headerText.innerHTML = text;
    //     headerText.classList.add(`${text}`)
    //     headerText.setAttribute('onclick', `sortCol(this, "${index}")`)
    //     headerRow.appendChild(headerText);
    //     table.appendChild(headerRow);

    // });

    // Data to table

    editedData.forEach(item => {
        let dataRow = document.createElement("tr");
        for (const key in item) {
            let dataText = document.createElement("td");
            dataText.innerText = item[key];
            dataRow.appendChild(dataText);
            tableBox.appendChild(dataRow);
            
        }
    })
    // tableBox.appendChild(table);
    

}

// Sorting

lastSortBy = 'broj';
const sortCol = (headerName, index) => {
    if (headerName == lastSortBy) {
        sortDirection = !sortDirection;
    } else {
        sortDirection = false;
    }

    lastSortBy = headerName;
    // sortDirection = !sortDirection;
    const dataType = typeof(data[index][headerName]);
    switch (dataType) {
        case 'number':
            sortNumberCol(sortDirection, headerName);
            break;
        case 'string':
            sortStringCol(sortDirection, headerName)
            break;
    }
};  

const sortNumberCol = (sort, header) => {
    data = data.sort((a, b) => {
        return sort ? a[header] - b[header] : b[header] - a[header];
    });
    pagination(0)
}

const sortStringCol = (sort, header) => {
    data = data.sort((a, b) => {
        return sort ? (a[header] > b[header]) - (a[header] < b[header]) : (b[header] > a[header]) - (b[header] < a[header])
    });
    pagination(0);
}


// Pagination

let brojDana = document.querySelector('.broj-dana');
let showMoreBtn = document.querySelector('.show-more');
const pagination = (index) => {
    
    if (index < 0) {
        createTable(data);
    }
    else {
        let pagData = []
        for (let i = 0; i < index + 1; i++) {
            data.forEach(item => {
                if (item['datum'] == dates[i])
                    pagData.push(item)
            });
        }
        createTable(pagData);
    }
        
};
showMoreBtn.addEventListener('click', () => {
    let currentPage = parseInt(brojDana.innerText);
    console.log(dates.length)
    if (currentPage < dates.length)
        brojDana.innerText = currentPage + 1;
        pagination(brojDana.innerText - 1)
});
let submitBtn = document.getElementById('submit');
// nextBtn.addEventListener('click', () => {
//     let currentPage = parseInt(pageNum.innerText);
    
//     if (parseInt(pageNum.innerText) <= (~~(data.length / numItems))) {
//         pageNum.innerText = currentPage + 1;
//         pagination(pageNum.innerText); 
//     }
// });

// previousBtn.addEventListener('click', () => {
//     let currentPage = parseInt(pageNum.innerText);
//     if (currentPage > 1) {
//         pageNum.innerText = currentPage - 1;
//         pagination(pageNum.innerText);
//     };
// });


function test() {
    let queryBroj = document.getElementById('broj').value;
    let queryStartDate = document.getElementById('start').value;
    let queryEndDate = document.getElementById('end').value;
    let queryPrimalac = document.querySelector('.primalac').value;
    let queryPosiljalac = document.querySelector('.posiljalac').value;
    let queryPorucilac = document.querySelector('.porucilac').value;
    let queryArtikal = document.querySelector('.artikal').value;
    let queryPrevoznik = document.querySelector('.prevoznik').value;
    let queryRegistracija = document.querySelector('.registracija').value;
    let q = {};
    if (queryBroj != '') {
        q['broj'] = `${queryBroj}`;
    }
    if (queryPosiljalac != '') {
        q['posiljalac'] = `${queryPosiljalac}`;
    }
    if (queryPrimalac != '') {
        q['primalac'] = `${queryPrimalac}`;
    }
    if (queryPorucilac != '') {
        q['porucilac'] = `${queryPorucilac}`;
    }
    if (queryArtikal != '') {
        q['artikal'] = `${queryArtikal}`;
    }
    if (queryPrevoznik != '') {
        q['prevoznik'] = `${queryPrevoznik}`;
    }
    if (queryRegistracija != '') {
        q['registracija'] = `${queryRegistracija}`;
    }
    if (queryStartDate != '') {
        q['datumStart'] = `${queryStartDate}`;
    }
    if (queryEndDate != '') {
        q['datumEnd'] = `${queryEndDate}`;
    }
    // console.log(new URLSearchParams(q).toString())
    // fetch('/izvestaj?' + new URLSearchParams(q));
    window.location.href = '/izvestaj?' + new URLSearchParams(q);
}

function deleteFile(file) {
    fetch(`/files/${file}`, {
        method: 'DELETE',
    }).then(() => {
        window.location.href = "/files"
    })
}
