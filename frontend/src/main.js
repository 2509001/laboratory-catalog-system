import {
    renderEquipmentCatalog,
    setupSearch,
    setupStatusUpdate
} from "./pages/EquipmentCatalog.js";

async function start() {

    document.getElementById("app").innerHTML =
        await renderEquipmentCatalog();

    await setupSearch();

    setupStatusUpdate();

}

start();