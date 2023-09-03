$(() => {
    const url = "http://127.0.0.1:5000";
  
    $('#gridContainer').dxDataGrid({
      dataSource: DevExpress.data.AspNet.createStore({
        key: 'id',
        loadUrl: url + "/Dados/Cor",
        insertUrl: url + "/Dados/Cor",
        updateUrl: url + "/Dados/Cor",
        deleteUrl: url + "/Dados/Cor",
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
          caption: 'Cor',
          validationRules: [{ type: 'required' }],
        }
      ],
    });
  });
  