import {
    renderEquipmentCatalog,
    setupSearch
} from "./pages/EquipmentCatalog.js";

async function start() {

    document.getElementById("app").innerHTML =
        await renderEquipmentCatalog();

    await setupSearch();
}

start();