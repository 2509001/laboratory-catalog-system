import {
  renderEquipmentForm,
  setupEquipmentForm
} from "./pages/EquipmentForm.js";

document.getElementById("app").innerHTML =
  renderEquipmentForm();

setupEquipmentForm();