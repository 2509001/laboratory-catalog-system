const API_URL = "http://127.0.0.1:8000";

export async function createEquipment(data) {
    const response = await fetch(
        `${API_URL}/equipment`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    return response.json();
}

export async function getEquipment() {
    const response = await fetch(
        `${API_URL}/equipment`
    );

    return response.json();
}

export async function updateEquipmentStatus(
    equipmentId,
    operationalStatus
) {

    const response = await fetch(
        `${API_URL}/equipment/${equipmentId}/status`,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                operational_status: operationalStatus
            })
        }
    );

    return response.json();
}