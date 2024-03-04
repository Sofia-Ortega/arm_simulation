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
document.body.appendChild(renderer.domElement);

// ************ Creating Shapes ******************
// create cube
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// create line
const lineMaterial = new THREE.LineBasicMaterial({ color: 0xa1a1ff });
const points = [];
points.push(new THREE.Vector3(-10, 0, 0));
points.push(new THREE.Vector3(0, 10, 0));
points.push(new THREE.Vector3(10, 0, 0));
const lineGeometry = new THREE.BufferGeometry().setFromPoints(points);
const line = new THREE.Line(lineGeometry, lineMaterial);
scene.add(line);
//renderer.render(scene, camera);

function animate() {
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    line.rotateX(0.01);
    line.rotateY(0.005);

    renderer.render(scene, camera);
}
animate();
