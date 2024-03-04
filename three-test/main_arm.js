// Import Three.js
import * as THREE from "three";

// Import GLTFLoader
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

// Setup Three.js Scene
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Adding Lights
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(0, 1, 1);
scene.add(directionalLight);

// Loading GLTF Model
const loader = new GLTFLoader();
loader.load(
    "/scene.gltf",
    function (gltf) {
        const model = gltf.scene;
        scene.add(model);
        console.log(model);

        // Position and Orient the Camera to Look at the Model
        const box = new THREE.Box3().setFromObject(model); // Calculate the bounding box of the model
        const center = box.getCenter(new THREE.Vector3()); // Get the center of the bounding box
        const size = box.getSize(new THREE.Vector3()); // Get the size of the bounding box

        camera.position.copy(center); // Set camera position to the center of the model
        camera.position.z = Math.max(size.x, size.y, size.z) * 2; // Adjust camera distance based on the size of the model
        camera.lookAt(center); // Make the camera look at the center of the model
    },
    undefined,
    function (error) {
        console.error(error);
    }
);

// Position and Rotate the Camera
camera.position.z = 5;

// Render Loop
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();
