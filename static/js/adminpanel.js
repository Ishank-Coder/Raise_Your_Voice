// Load Google Charts library
google.charts.load('current', { 'packages': ['corechart', 'bar'] });
google.charts.setOnLoadCallback(handleCheckboxSelection);

// Sample data (replace with your actual data)
var data = {
    'pieChart':{
        'examCheckbox': [
            ['Category', 'Value'],
            ['New Tickets', 10],
            ['Ongoing Tickets', 20],
            ['Closed Tickets', 30],
        ],
        'disciplineCheckbox': [
            ['Category', 'Value'],
            ['New Tickets', 5],
            ['Ongoing Tickets', 12],
            ['Closed Tickets', 10],
        ],
        'antiRaggingCheckbox': [
            ['Category', 'Value'],
            ['New Tickets', 12],
            ['Ongoing Tickets', 20],
            ['Closed Tickets', 15],
        ],
        'womenCheckbox': [
            ['Category', 'Value'],
            ['New Tickets', 15],
            ['Ongoing Tickets', 8],
            ['Closed Tickets', 14],
        ],
        'defaultData': [
            ['Task', 'Tickets Status'],
            ['New Tickets', 8],
            ['Ongoing Tickets', 12],
            ['Closed Tickets', 4],
        ],
    },    
    'daywiseBarChart': {
        'examCheckbox': [
            ['Date', 'Exam', 'Discipline', 'AntiRagging', 'Women'],
            ['17-09-2023', 1, 2, 6, 8],
            ['18-09-2023', 4, 11, 9, 6],
            ['19-09-2023', 8, 7, 7, 7],
            ['20-09-2023', 2, 5, 6, 6],
            ['21-09-2023', 13, 9, 2, 10],
        ],
        'disciplineCheckbox': [
            ['Date', 'Exam', 'Discipline', 'AntiRagging', 'Women'],
            ['17-09-2023', 2, 9, 5, 8],
            ['18-09-2023', 4, 21, 9, 6],
            ['19-09-2023', 8, 7, 7, 7],
            ['20-09-2023', 2, 8, 5, 9],
            ['21-09-2023', 13, 9, 2, 10],
        ],
        'antiRaggingCheckbox': [
            ['Date', 'Exam', 'Discipline', 'AntiRagging', 'Women'],
            ['17-09-2023', 3, 9, 5, 8],
            ['18-09-2023', 4, 11, 9, 9],
            ['19-09-2023', 8, 7, 7, 7],
            ['20-09-2023', 2, 5, 6, 8],
            ['21-09-2023', 13, 9, 2, 10],
        ],
        'womenCheckbox': [
            ['Date', 'Exam', 'Discipline', 'AntiRagging', 'Women'],
            ['17-09-2023', 4, 9, 5, 8],
            ['18-09-2023', 4, 11, 9, 6],
            ['19-09-2023', 8, 7, 7, 7],
            ['20-09-2023', 2, 5, 6, 6],
            ['21-09-2023', 13, 9, 2, 10],
        ],
        'defaultData': [
            ['Date', 'Exam', 'Discipline', 'AntiRagging', 'Women'],
            ['17-09-2023', 5, 9, 5, 8],
            ['18-09-2023', 4, 11, 9, 6],
            ['19-09-2023', 8, 7, 7, 7],
            ['20-09-2023', 2, 5, 6, 6],
            ['21-09-2023', 13, 9, 2, 10],
        ],
    },
};

function handleCheckboxSelection(checkboxId) {
    // Uncheck all checkboxes
    const checkboxes = document.querySelectorAll('.check');
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    });

    // Check the selected checkbox
    const selectedCheckbox = document.getElementById(checkboxId);
    drawCharts(checkboxId);
    // drawCharts2(checkboxId);
    drawCharts1(checkboxId);
    
    if (selectedCheckbox) {
        selectedCheckbox.checked = true;
        // Store the ID of the selected option in the "choose" variable
        choose = checkboxId;
        // Update the charts based on the selected category
        // updateCharts(choose);
    }
}
// Function to draw charts
function drawCharts(choose) {
    if (choose == 'examCheckbox') {
        drawPieChart(data.pieChart.examCheckbox);  
    }
    else if (choose == 'disciplineCheckbox') {
        drawPieChart(data.pieChart.disciplineCheckbox);  
    }
    else if (choose == 'antiRaggingCheckbox') {
        drawPieChart(data.pieChart.antiRaggingCheckbox);  
    }
    else if (choose == 'womenCheckbox') {
        drawPieChart(data.pieChart.womenCheckbox);  
    }
    else
    {
        drawPieChart(data.pieChart.defaultData);
    }
}
function drawCharts1(choose) {
    if (choose == 'examCheckbox') {
        drawDaywiseBarChart(data.daywiseBarChart.examCheckbox);  
    }
    else if (choose == 'disciplineCheckbox') {
        drawDaywiseBarChart(data.daywiseBarChart.disciplineCheckbox);  
    }
    else if (choose == 'antiRaggingCheckbox') {
        drawDaywiseBarChart(data.daywiseBarChart.antiRaggingCheckbox);  
    }
    else if (choose == 'womenCheckbox') {
        drawDaywiseBarChart(data.daywiseBarChart.womenCheckbox);  
    }
    else
    {
        drawDaywiseBarChart(data.daywiseBarChart.defaultData);
    
    }
}


// Function to draw Pie Chart
function drawPieChart(chartData) {
    console.log("drawpieChart called with data:", chartData);
    var dataTable = google.visualization.arrayToDataTable(chartData);

    var options = {
        title: 'Tickets Status',
        is3D: true,
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(dataTable, options);
}

// Function to draw Day-wise Bar Chart
function drawDaywiseBarChart(chartData) {
    console.log("drawDaywiseBarChart called with data:", chartData);
    var dataTable = google.visualization.arrayToDataTable(chartData);

    var options = {
        title: 'Day-wise Tickets',
        chartArea: { width: '80%' },
        hAxis: { title: 'Date' },
        vAxis: { title: 'Tickets' },
        legend: { position: 'top' },
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('daywise-chart'));
    chart.draw(dataTable, options);
}


