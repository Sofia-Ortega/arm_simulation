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

const pivotPoint = new THREE.Vector3(2, 20, 2);

function animate() {
    requestAnimationFrame(animate);

    cube.position.sub(pivotPoint);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    cube.position.add(pivotPoint);
    // cube.rotation.x += 0.01;

    renderer.render(scene, camera);
}
animate();
