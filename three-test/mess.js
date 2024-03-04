import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

camera.position.set(0, 0, 100);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true; // Enable shadow mapping
document.body.appendChild(renderer.domElement);

// Add directional light for casting shadows
const light = new THREE.DirectionalLight(0xffffff, 1.2);
const light2 = new THREE.AmbientLight();
light.position.set(-7, 10, 5);
scene.add(light);
scene.add(light2);

const geometry = new THREE.BoxGeometry(2, 20, 2);
const material = new THREE.MeshStandardMaterial({ color: 0x76a0f5 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

const anchorPoint = new THREE.Object3D(); // Create an anchor point object
scene.add(anchorPoint); // Add the anchor point to the scene

function animate() {
    requestAnimationFrame(animate);

    // Calculate rotation angle based on time
    const time = Date.now() * 0.0001; // Convert milliseconds to seconds
    const angle = time * Math.PI * 2; // Rotate at 1 full rotation per second

    // Calculate the position of the rotating side around the circle
    const radius = 30; // Radius of the circle
    const x = Math.cos(angle) * radius;
    const y = Math.sin(angle) * radius;

    // Set the position of the rotating side of the rectangle
    cube.position.set(x, y, 0);

    // Set the position of the fixed side of the rectangle (anchor point)
    //anchorPoint.position.set(0, 0, 0);

    // Look at the anchor point (center of the scene)
    cube.lookAt(anchorPoint.position);

    renderer.render(scene, camera);
}
animate();
