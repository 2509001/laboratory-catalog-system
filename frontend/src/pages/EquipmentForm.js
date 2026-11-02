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
  `;
}