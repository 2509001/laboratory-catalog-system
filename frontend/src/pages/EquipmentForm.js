import { createEquipment } from "../services/api.js";

export function renderEquipmentForm() {
  return `
    <h1>Register Equipment</h1>

    <form id="equipment-form">

      <input
        type="text"
        id="officialInventoryNumber"
        placeholder="Official Inventory Number"
      />

      <input
        type="text"
        id="internalLabNumber"
        placeholder="Internal Lab Number"
      />

      <input
        type="text"
        id="name"
        placeholder="Equipment Name"
      />

      <input
        type="text"
        id="brand"
        placeholder="Brand"
      />

      <input
        type="text"
        id="model"
        placeholder="Model"
      />

      <button type="submit">
        Save Equipment
      </button>

    </form>

    <p id="message"></p>
  `;
}

export function setupEquipmentForm() {
  const form = document.getElementById("equipment-form");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const equipment = {
      official_inventory_number:
        document.getElementById("officialInventoryNumber").value,

      internal_lab_number:
        document.getElementById("internalLabNumber").value,

      name:
        document.getElementById("name").value,

      brand:
        document.getElementById("brand").value,

      model:
        document.getElementById("model").value,

      location: "Electronics Lab",
      operational_status: "Operational",

      category_id:
        "21115104-ed77-40c8-87c1-32391dfb6c94"
    };

    const result = await createEquipment(
      equipment
    );

    document.getElementById("message").textContent =
      result.message;
  });
}