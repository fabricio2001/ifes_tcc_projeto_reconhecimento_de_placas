$(() => {
  const url = "http://127.0.0.1:5000";

  const source = new DevExpress.data.DataSource({
    load() {
      return $.getJSON(url + "/Chart/Entrada");
    },
    loadMode: 'raw',
    filter: ['ParentID', '=', null],
    paginate: false,
  });



  let isFirstLevel = true;
  const chartContainer = $('#chart');
  const chart = chartContainer.dxChart({
    dataSource: filterData(''),
    title: 'Entrada de Carros',
    series: {
      type: 'bar',
    },
    legend: {
      visible: false,
    },
    valueAxis: {
      showZero: false,
    },
    onPointClick(e) {
      if (isFirstLevel) {
        isFirstLevel = false;
        removePointerCursor(chartContainer);
        // console.log(e.target.originalArgument);
        chart.option({
          dataSource: filterData(e.target.originalArgument),
        });
        // refreshDataSource(e.target.originalArgument);
        $('#backButton')
          .dxButton('instance')
          .option('visible', true);
      }
    },
    customizePoint() {
      const pointSettings = {
        color: colors[Number(isFirstLevel)],
      };

      if (!isFirstLevel) {
        pointSettings.hoverStyle = {
          hatching: 'none',
        };
      }

      return pointSettings;
    },
  }).dxChart('instance');

  $('#backButton').dxButton({
    text: 'Back',
    icon: 'chevronleft',
    visible: false,
    onClick() {
      if (!isFirstLevel) {
        isFirstLevel = true;
        addPointerCursor(chartContainer);
        chart.option('dataSource', filterData(''));
        chartContainer.dxChart("instance").getDataSource().load();
        this.option('visible', false);
      }
    },
  });

  addPointerCursor(chartContainer);
});

function filterData(name) {
  return data.filter((item) => item.parentID === name);
}

function addPointerCursor(container) {
  container.addClass('pointer-on-bars');
}

function removePointerCursor(container) {
  container.removeClass('pointer-on-bars');
}

function refreshDataSource(argument) {
  var dataSource = $("#chart").dxChart("instance").getDataSource();

  dataSource.filter(["ParentID", argument]);
  dataSource.load();
}