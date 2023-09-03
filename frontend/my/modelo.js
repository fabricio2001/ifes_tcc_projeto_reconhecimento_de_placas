$(() => {
    const url = "http://127.0.0.1:5000";
  
    $('#gridContainer').dxDataGrid({
      dataSource: DevExpress.data.AspNet.createStore({
        key: 'id',
        loadUrl: url + "/Dados/Modelo",
        insertUrl: url + "/Dados/Modelo",
        updateUrl: url + "/Dados/Modelo",
        deleteUrl: url + "/Dados/Modelo",
        onBeforeSend(method, ajaxOptions) {
          ajaxOptions.xhrFields = { withCredentials: false };
        },
      }),
      columnsAutoWidth: true,
      rowAlternationEnabled: true,
      showBorders: true,
      filterRow: {
        visible: true,
        applyFilter: 'auto',
      },
      searchPanel: {
        visible: true,
        width: 240,
        placeholder: 'Pesquisa...',
      },
      headerFilter: {
        visible: true,
      },
      paging: {
        enabled: false,
      },
      editing: {
        mode: 'form',
        allowUpdating: true,
        allowAdding: true,
        allowDeleting: true,
      },
      columns: [
        {
          dataField: 'nome',
          caption: 'Modelo',
          validationRules: [{ type: 'required' }],
        }
      ],
    });
  });
  