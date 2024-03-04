import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    2000
);
camera.position.set(0, 0, 5);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const loader = new GLTFLoader();

loader.load(
    "/scene.gltf",
    function (gltf) {
        gltf.scene.scale.set(1000, 1000, 1000);

        scene.add(gltf.scene);
    },
    undefined,
    function (error) {
        console.error(error);
    }
);

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();
